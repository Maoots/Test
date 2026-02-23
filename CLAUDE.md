# CLAUDE.md

This file provides guidance for AI assistants (Claude and others) working in this repository.

## Repository Status

This is a freshly initialized repository. No source code, tests, or configuration files exist yet. This CLAUDE.md will be updated as the project evolves.

## Git Configuration

- **Remote origin:** `http://local_proxy@127.0.0.1:36702/git/Maoots/Test`
- **Default working branch pattern:** `claude/claude-md-*`
- **Commit signing:** Enabled via SSH key

## Development Branch Conventions

- Feature branches follow the pattern: `claude/<description>-<session-id>`
- Always push to the designated feature branch, never directly to `main` or `master`
- Use `git push -u origin <branch-name>` when pushing for the first time

## Git Workflow

```bash
# Check current branch before making changes
git branch

# Stage specific files (avoid staging unintended files)
git add <file1> <file2>

# Commit with a descriptive message
git commit -m "feat: describe what was added or changed"

# Push to the feature branch
git push -u origin <branch-name>
```

### Commit Message Format

Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

| Prefix | When to use |
|--------|-------------|
| `feat:` | New feature or functionality |
| `fix:` | Bug fix |
| `docs:` | Documentation changes only |
| `refactor:` | Code restructuring without behavior change |
| `test:` | Adding or updating tests |
| `chore:` | Maintenance tasks (deps, config, build) |
| `ci:` | CI/CD pipeline changes |

## Project Setup (To Be Defined)

Once a technology stack is chosen, update this file with:

- **Language & runtime** (e.g., Node.js 20, Python 3.12, Go 1.22)
- **Package manager** (e.g., npm, pnpm, yarn, pip, cargo)
- **How to install dependencies**
- **How to run the project locally**
- **How to run tests**
- **How to lint and format code**

### Template: Common Setup Commands

```bash
# Node.js / JavaScript / TypeScript
npm install          # Install dependencies
npm run dev          # Start development server
npm test             # Run tests
npm run lint         # Lint code
npm run build        # Build for production

# Python
pip install -e ".[dev]"   # Install with dev dependencies
python -m pytest          # Run tests
ruff check .              # Lint
ruff format .             # Format

# Go
go mod download       # Install dependencies
go test ./...         # Run tests
go vet ./...          # Lint
go build ./...        # Build
```

## File & Directory Conventions (To Be Defined)

Update this section once the project structure is established. Common patterns:

```
<project-root>/
├── src/              # Application source code
├── tests/            # Test files
├── docs/             # Documentation
├── scripts/          # Utility/automation scripts
├── .github/          # GitHub Actions CI/CD
├── CLAUDE.md         # This file
└── README.md         # Human-facing project overview
```

## Code Style & Quality (To Be Defined)

Document linting and formatting rules once configured. Key areas to capture:

- **Formatter** (e.g., Prettier, Black, gofmt) and whether it runs automatically
- **Linter** (e.g., ESLint, Ruff, golangci-lint) and any rule overrides
- **Type checking** (e.g., TypeScript strict mode, mypy, pyright)
- **Pre-commit hooks** and what they enforce

## Testing Conventions (To Be Defined)

Once tests exist, document:

- **Test runner** and how to invoke it
- **Coverage requirements** (e.g., minimum 80%)
- **Test file naming** (e.g., `*.test.ts`, `test_*.py`, `*_test.go`)
- **Where to place tests** (co-located vs. separate `tests/` directory)
- **How to run a single test file or test case**

## Environment Variables (To Be Defined)

Document required environment variables once they exist:

```bash
# Copy the example env file and fill in values
cp .env.example .env
```

List all required variables with descriptions once known.

## AI Assistant Guidelines

### General Principles

- **Read before modifying.** Always read a file before editing it. Never modify code you haven't inspected.
- **Minimal changes.** Make only the changes necessary to complete the task. Avoid refactoring unrelated code.
- **No speculative features.** Do not add error handling, logging, or validation for hypothetical scenarios. Only address real, present requirements.
- **No unused code.** Delete removed code entirely rather than commenting it out or renaming with `_old`.
- **Security.** Never commit secrets, API keys, or credentials. Never introduce SQL injection, XSS, command injection, or other OWASP Top 10 vulnerabilities.

### When Working in This Repository

1. Check which branch you are on before starting work (`git branch`)
2. Use the branch specified in the task description
3. Make focused, atomic commits
4. Push to the designated branch when done
5. Update this CLAUDE.md whenever the project structure or conventions change significantly

### What to Update in This File

As the project grows, keep CLAUDE.md current by updating:

- Build and test commands when they change
- New environment variables or configuration requirements
- Architectural decisions and the reasoning behind them
- Any non-obvious conventions or gotchas specific to this codebase
- Deprecations or breaking changes that affect how AI assistants should work

## Updating This File

This file should be updated whenever:
- A new technology, framework, or tool is added to the project
- Build, test, or lint commands change
- A new architectural pattern or convention is adopted
- Environment variable requirements change
- Something non-obvious trips up a developer (human or AI)
