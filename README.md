# polyforge-sandbox

A tiny repository used for polyforge clean-room acceptance runs (a real
develop ticket from filing to a merged PR). Changes here are harmless by
design; nothing depends on this repository.

- `greet.py` — one function.
- `test_greet.py` — its tests: `python3 -m unittest -v`.

`greet(name)` trims leading and trailing whitespace using Python's `str.strip()`,
including Unicode whitespace. Empty or whitespace-only names default to `world`.
Whitespace inside a name stays unchanged, including repeated spaces and tabs.
Ordinary names such as `polyforge` keep their existing greeting.

The CLI uses `world` when no argument is supplied:

```console
$ python3 greet.py
Hello, world!
$ python3 greet.py '  polyforge  '
Hello, polyforge!
$ python3 greet.py ''
Hello, world!
```

The `.polyforge` verification declarations run the standard-library tests and
check both required CLI examples. No application dependencies are needed.
