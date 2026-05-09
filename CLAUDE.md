# Repository Guidance for Claude Code

## Cross-conversation safety

Anything under `.claude/worktrees/` belongs to whichever Claude session created it — including the worktree directory itself and the branch checked out there. **Never delete or modify these from another session**, even when the branch has been merged into `main`.

If cleanup of a worktree under `.claude/worktrees/` appears needed (for example, when the user asks to "sync main and clean up merged branches"), surface it as a question for the user to decide rather than removing it automatically.

Local branches that are **not** checked out in a separate worktree are not subject to this rule — they can be auto-deleted once their PR is merged.
