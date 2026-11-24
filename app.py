"""Local Streamlit human-review demonstration."""
import csv
import io
import streamlit as st
from agentguard.core import inspect_action, load_scenarios, requires_approval

st.set_page_config(page_title='AgentGuard', page_icon='🛡️')
st.title('🛡️ AgentGuard — Human Oversight Lab')
st.caption('Synthetic demonstrations only. No real file operations or messages.')
label = st.radio('Approval policy', ['Every action', 'Sensitive actions only'], horizontal=True)
policy = 'every_action' if label == 'Every action' else 'sensitive_only'
evidence = st.checkbox('Show rule evidence and checker findings', value=True)
items = [s for s in load_scenarios() if requires_approval(s, policy)]
records = []
for s in items:
    with st.expander(f'{s["id"]} — {s["description"]}'):
        st.write('**Proposed action:**', s['action'])
        st.write('**Target:**', s['target'])
        if evidence:
            st.write('**Expected target:**', s['expected_target'])
            st.write('**Required evidence:**', ', '.join(s['required_evidence']) or 'None')
            st.write('**Provided evidence:**', ', '.join(s['provided_evidence']) or 'None')
            st.write('**Checker flags:**', ', '.join(inspect_action(s)) or 'None')
        decision = st.radio('Reviewer decision', ['Not reviewed', 'Approve', 'Reject'], key=s['id'], horizontal=True)
        records.append({'id': s['id'], 'policy': policy, 'evidence_shown': evidence,
                        'decision': decision, 'checker_flagged': bool(inspect_action(s))})
st.metric('Approval prompts', len(items))
st.metric('Decisions recorded', sum(r['decision'] != 'Not reviewed' for r in records))
if records:
    data = io.StringIO()
    writer = csv.DictWriter(data, fieldnames=list(records[0]))
    writer.writeheader()
    writer.writerows(records)
    st.download_button('Export reviewer decisions as CSV', data.getvalue(), 'agentguard_reviews.csv', 'text/csv')
st.caption('Checker flags are not human detections. No empirical study has been conducted.')
