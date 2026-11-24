# Beyond the Approval Button: Evidence and Context in Agent Oversight

*Original technical explainer; not an empirical paper.*

An autonomous office assistant can execute a requested task correctly while still making a consequential mistake. Imagine an agent attaching the right report to an email but selecting the wrong recipient. From the perspective of task completion, the workflow appears successful; from the perspective of confidentiality, it fails. Reliable oversight therefore requires attention to both successful execution and safeguard compliance.

## The approval trade-off

An approval-before-every-action system presents many opportunities to intervene. However, it also interrupts ordinary actions, potentially increasing review burden. Selective approval prompts only for actions labelled sensitive, such as sharing or deletion. Whether this reduces fatigue or preserves detection requires empirical testing; fewer prompts alone do not establish safer oversight. A wrong-folder move, for instance, can be missed by a simplistic sensitivity rule.

## Evidence matters, but is not sufficient

A prompt that names only the action may be less informative than one showing the applicable rule, approved recipient and verification evidence. But a more detailed prompt could also create clutter or encourage overreliance on automated checks. This is an empirical human–AI interaction question, not a settled design principle.

A useful interface keeps four concepts separate: what action is proposed, which rule applies, what evidence supports compliance, and what the reviewer decided. Missing evidence should not automatically be confused with evidence that a violation occurred.

## How to evaluate

A simulated office study can use invented files and identities, introduce controlled errors, and compare approval policies over matched tasks. Researchers should record actual reviewer responses, false positives, time, and prompt burden. Approval opportunities are not the same as detected errors. Counterbalancing and preregistered analysis help separate interface effects from task order and learning.

## Governance relevance

Oversight is also an accountability problem. A useful audit trail should preserve the proposed action, the governing rule, supporting evidence and a human decision—without leaking sensitive information. AgentGuard provides a transparent demonstration of these ideas; it does not establish that a policy or interface is safe in real deployments.
