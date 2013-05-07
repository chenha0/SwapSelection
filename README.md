SwapSelection
=============

This plugin aims at implementing an easy way to swap multi-selections in sublime
text 2.

Currently the plugin is under development.

Usage:
------
Swapping between two selections is easy. All of `alt + ]`, `alt + [`, `alt + =`
will do. 

Note that when it comes to 3 or more, the 3 shortcuts behave differentely.

Say each of the words following are selected separately:

```
foo bar baz
```

1) By typing `alt + ]`, the order is changed to:

```
baz foo bar
```

The selections are cycling-shuffled to right direction.

2) By typing `alt + [`, the order is changed to:

```
bar baz foo
```

The selections are cycling-shuffled to left direction.

3) By typing `alt + =`, the order is changed to:

```
baz bar foo
```

The selections are reversely placed.
