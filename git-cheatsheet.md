# My Git Cheat Sheet

**Created:** January 21, 2026  
**Purpose:** Quick reference for Git commands I use regularly

---

## 🔧 Initial Setup (One-Time Only)

### Install Git
1. Download from: https://git-scm.com
2. Install with defaults
3. Verify: `git --version`

### Configure Git (First time only)
```bash
git config --global user.name "Gavin Beck"
git config --global user.email "biaandgav@gmail.com"
```

### Setup SSH Keys (First time only)

**Generate SSH key:**
```bash
ssh-keygen -t ed25519 -C "biaandgav@gmail.com"
# Press Enter for default location
# Press Enter twice for no passphrase
```

**Copy public key (Windows):**
```bash
type C:\Users\166308\.ssh\id_ed25519.pub
```

**Add to GitHub:**
1. Go to GitHub → Settings → SSH and GPG keys
2. Click "New SSH key"
3. Paste the public key
4. Save

**Test connection:**
```bash
ssh -T git@github.com
# Should say: "Hi GavinBeck99! You've successfully authenticated..."
```

---

## 📥 Clone Repository (First Time)

**When you want to work on a repo for the first time:**
```bash
# Navigate to where you want the code
cd Documents

# Clone the repository
git clone git@github.com:GavinBeck99/repository-name.git

# Enter the repository
cd repository-name
```

**Example with my learning-journey repo:**
```bash
cd Documents
git clone git@github.com:GavinBeck99/learning-journey.git
cd learning-journey
```

---

## 🔄 Daily Git Workflow

**This is what you'll do EVERY time you work:**

### 1. Check Status (Always start here!)
```bash
git status
# Shows: what branch you're on, what's changed
```

### 2. Pull Latest Changes (if working with others or multiple computers)
```bash
git pull
# Gets latest changes from GitHub
```

### 3. Create/Edit Files
- Make your changes in Cursor or any editor
- Save your files

### 4. Check What Changed
```bash
git status
# See what files changed

git diff
# See exactly what lines changed
```

### 5. Stage Changes
```bash
# Stage specific file:
git add filename.md

# OR stage everything:
git add .
```

### 6. Commit Changes
```bash
git commit -m "Clear description of what you changed"
```

**Good commit messages:**
- "Add Tuesday learning log"
- "Fix typo in README"
- "Update Git cheatsheet with new commands"

### 7. Push to GitHub
```bash
git push
```

### 8. Verify
```bash
git status
# Should say: "Your branch is up to date with 'origin/main'"
```

---

## 🌲 Working with Branches

### See All Branches
```bash
git branch
# * shows current branch
```

### Create and Switch to New Branch
```bash
git checkout -b branch-name
# Example: git checkout -b add-tuesday-log
```

### Switch to Existing Branch
```bash
git checkout branch-name
# Example: git checkout main
```

### Merge Branch into Current Branch
```bash
# First, switch to the branch you want to merge INTO (usually main)
git checkout main

# Then merge the feature branch
git merge branch-name
```

### Delete Branch (after merging)
```bash
git branch -d branch-name
```

---

## 🆘 Common Problems & Solutions

### "Permission denied (publickey)"
**Problem:** SSH key not set up or not working  
**Solution:** 
1. Check SSH key exists: `ls ~/.ssh/id_ed25519.pub`
2. If not, generate new one (see Setup SSH Keys above)
3. Make sure it's added to GitHub

### "fatal: not a git repository"
**Problem:** You're not in a Git repository folder  
**Solution:** 
```bash
cd path/to/your/repository
# Example: cd Documents/learning-journey
```

### "Your branch is ahead of 'origin/main' by X commits"
**Problem:** You have local commits not pushed to GitHub  
**Solution:** `git push`

### "Your branch is behind 'origin/main'"
**Problem:** GitHub has changes you don't have locally  
**Solution:** `git pull`

### Made changes on wrong branch
**Problem:** Edited files on main instead of feature branch  
**Solution:**
```bash
# Stash your changes
git stash

# Switch to correct branch
git checkout correct-branch

# Apply your changes
git stash pop
```

---

## 📍 Quick Reference - Most Common Commands
```bash
git status              # Check what's changed
git add .               # Stage all changes
git commit -m "msg"     # Commit with message
git push                # Push to GitHub
git pull                # Get latest from GitHub
git checkout -b name    # Create new branch
git checkout main       # Switch to main branch
git branch              # List all branches
git merge branch-name   # Merge branch into current
```

---

## 🔗 Useful Resources

**When I forget something:**
- My cheat sheet (this file!)
- GitHub Docs: https://docs.github.com/en/get-started/using-git
- Git visualization: https://learngitbranching.js.org/
- Ask Claude: "How do I [specific task] with Git?"

**Search terms that work:**
- "git clone ssh"
- "git push to github"
- "git create branch"
- "git ssh key setup github"

---

## 📝 Personal Notes

**Things I found tricky:**
- Need to restart PowerShell after installing Node.js
- SSH key must be added to GitHub Settings, not just generated
- `git add .` stages ALL changes (be careful!)
- Always check `git status` before committing

**Shortcuts I use:**
- `git add .` instead of adding files individually
- `git checkout -b name` instead of `git branch` then `git checkout`

**My workflow in practice:**
1. Open PowerShell
2. `cd Documents/learning-journey`
3. `git status` (check I'm on right branch)
4. Make changes in Cursor
5. `git add .`
6. `git commit -m "what I did"`
7. `git push`
8. Done!

---

**Last Updated:** January 21, 2026
