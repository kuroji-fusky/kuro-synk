# kurosynk

A helper utility to check if shared code is outdated


The purpose of kurosynk is too make sure that shared components and utilities are in sync with each other, all without the hastle of manually tracking file(s) from repositories and branches.

The reason for creating this monstrosity is because:

- While code duplication from across projects is present, there's a select few that have specialized cases that would otherwise increase the complexity of the project
- To stop wasting time going through repos to find that one thing I need to copy-paste

**Why not use submodules/subtrees?**

Submodules, if used correctly, are great; some developers *loath* submodules due to how cumbersome it is. While some of my projects have submodules, I wouldn't heavily rely on it. Worst case scenario is to deal with merge conflicts from a submodule of all things.

**Why not publish your stuff to an npm registry?**

Yeah, nope. The code I write is just as bad to be publicly be shown from the registry. And even if I had my own private npm registry, I personally don't have time to set it up at this moment.

---

Call it over-engineering, sure, but honestly, if it keeps productivty at bay, then it works for me. Plus, I dunno what the hell I'm doing sometimes and just come up with a duct tape solutions like this one lol
