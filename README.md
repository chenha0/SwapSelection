SwapSelection
=============

This plugin aims at implementing an easy way to swap multi-selections in sublime
text 2.

Currently the plugin is under development.

Usage:
------

Say each of the words following are selected separately.

```
foo
bar
baz
```

By typing `alt + ]', the order is changed to:

```
baz
foo
bar
```
Swapping between two selections is plain to understand. However note that when it
comes to 3 or more, the swapping actually performs a shifting, which means the 
direction of shifting is sensitive.