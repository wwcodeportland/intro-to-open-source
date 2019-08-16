# Workshop: Intro to Open Source 🚀

This repo is for our Women Who Code 2017 Intro to Contributing to Open Source Workshop. This repo serves as a safe test space for those who wish to practice git, making pull requests and responding to issues.

## Workshop Agenda
 - Overviewing GitHub and Releases
 - Reviewing the Basics and Learning a Codebase
 - Your First Open Source Project Commit (look for First Timer's Only PRs)
 - What to expect - will my PR be merged in right away? How do deal with feedback?
 - Becoming a Regular Contributor

## Usage
In the `Issues` tab, we have a variety of issues with different labels that you can choose. Choose from any of the labels and submit a PR with your changes. We'll review your PR and conduct a mock code review, before ultimately merging your PR. 

If you have any questions about working in existing open source libraries, open a new issue!

## Git Config
First you should tell git your name and email (You can set specific ones for different repositories if you wish.). So if you're Scott Hanselman, you'd do it like this:
```
git config --global user.name "Scott Hanselman"
git config --global user.email scott@hanselman.com
```

If you want to set up a default editor you can set it using:
```
git config --global core.editor vim
```

To see what configuration settings you have:
```
git config --list
```

### Clone and fork this repo
Before contributing, fork this repo by pressing the "Fork" button inside the Women Who Code repo. This will create your own version of the repo.

To clone the respository down to your laptop, click the green clone or download button above and copy the link.

After copying the link, go to the path on your own computer that you want to clone this to. For organization it is more clear when there are separate directories for different repo owners.

### Making a new branch
Say you want to make changes on a branch other than master. This is common when wanting to separate different changes. If you want to have the exact

### Pulling down new content
In your terminal, run `git remote -v` to see all of your remotes. Add the Women Who Code repo as an upstream that you can pull from by adding the following:

`git remote add git@github.com:wwcodeportland/intro-to-open-source.git`

This will allow you to fetch the most recent changes from upstream.

* `git fetch`: fetches the changes, but doesn't merge them
* `git pull`: does `git fetch` and `git merge`. This results in an [extra commit](https://coderwall.com/p/7aymfa/please-oh-please-use-git-pull-rebase).
* `git pull --rebase`: leaves your commits in a straight line without branches

## Contributing to Open Source
### Creating an Issue
Click the button at the top that says "Issues" and then the green button to the right.
![create-issue](https://cloud.githubusercontent.com/assets/12282848/16970455/112131a4-4dd1-11e6-890b-697903e9b94b.png)

### Creating a Pull Request
Click the button at the top that says "Pull Requests" and then the green button to the right.
![create-pr](https://cloud.githubusercontent.com/assets/12282848/16970458/128818aa-4dd1-11e6-9388-f27a7106cb4e.png)
If the pull request (PR) is to fix an existing issue, you can reference it by `#somenumber`, e.g. `#2`. It's common to say "Fixes #somenumber" so when the PR is merged, it closes the corresponding issue.

*Tip: Include the issue the PR fixes in the commit message and have descriptive messages.*

### Resources
Great websites for people who are new to coding/contributing to open source:
* [First timers only](http://www.firsttimersonly.com/)
* [Your first PR](https://twitter.com/yourfirstpr)
* [Code Newbie](http://www.codenewbie.org/)
* [Get involved in tech](http://www.getinvolvedintech.com)

## Some Git/GitHub Resources
* [Official git documentation](https://git-scm.com/doc)
* [GitHub's Hello-World](https://guides.github.com/activities/hello-world/)
* [Brent Beer's OSCON talk: Everything I wish I knew when I started using GitHub](https://www.youtube.com/watch?v=KDUtjZHIx44)

## Contributing to an Open Source Project 
* [Open Source Guides](https://opensource.guide)
* [Course from egghead.io: How to Contribute to an Open Source Project on GitHub](https://egghead.io/courses/how-to-contribute-to-an-open-source-project-on-github)