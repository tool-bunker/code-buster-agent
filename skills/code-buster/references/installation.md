# Installing Code Buster

Check first:

```sh
cb version
```

Supported installation channels are documented at <https://toolbunker.dev/code-buster/docs/getting-started/installation>.

Common options:

```sh
brew install tool-bunker/tap/code-buster
dart pub global activate code_buster
```

For the verified native installer:

```sh
curl -fsSL https://codebuster.toolbunker.dev/install | sh
```

Ensure the selected installation directory is on `PATH`, then run `cb version` and `cb doctor`. Do not replace an existing installation or execute a remote installer without the user’s authorization.
