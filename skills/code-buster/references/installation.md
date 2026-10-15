# Installing Code Buster

Check first:

```sh
cb version
```

Supported installation channels are documented at <https://toolbunker.dev/codebuster/docs/getting-started/installation>.

Common options:

```sh
brew install tool-bunker/tap/code-buster
cargo install --git https://github.com/tool-bunker/code-buster.git --tag v0.9.0 --locked
```

The Cargo installation requires Rust 1.88 or newer. For a verified native
installer that does not require Rust:

```sh
curl -fsSL https://toolbunker.dev/codebuster/install | sh
```

Ensure the selected installation directory is on `PATH`, then run `cb version` and `cb doctor`. Do not replace an existing installation or execute a remote installer without the user’s authorization.
