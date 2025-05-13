## v0.1.8 (2025-05-13)

### Fix

- **allowlist**: bring back atterisk allow of UserLazyObject

## v0.1.7 (2025-05-13)

### Fix

- **internal**: convert auth database_sync_to_async to async def and remove some internal function type definition

## v0.1.6 (2025-05-05)

### Fix

- **allowlist**: readd UserLazyObject wildcard to allowlist

## v0.1.5 (2025-05-05)

### Fix

- **type,django**: corect some types and add django version constraints

## v0.1.4 (2025-05-03)

### Fix

- **pyright**: support pyright type hint with strict mode

## v0.1.3 (2025-05-01)

### Fix

- **origin_validator**: update allowed_origins to iterable instead of list of string

## v0.1.2 (2025-04-30)

### Fix

- **docs**: update readme and description

## v0.1.1 (2025-04-30)

### Fix

- **commitizen**: add pre bump hook for update lock before bump
- **readme**: update readme file
- **tox,auth**: add tox for multi environment testing and update async functions for auth
- **dev,workflow**: update dev relevant files and github workflow files

## v0.1.0 (2025-04-30)

### Feat

- **channels-stubs**: update message sent type to generic dict and the middleware protocol
- **python**: downgrade python version
- **stubs**: improve stub type correctness
- **channels-stubs**: write initial pyi files for the channels packages, which pass all stubtest
- **init**: initial package

### Fix

- **private-types**: make some types private to prevent mypy complaint about not present at runtime
