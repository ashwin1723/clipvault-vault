import git
from datetime import datetime

def backup_to_github():
    # Initialize Git in the vault folder
    repo = git.Repo.init("vault")
    
    # Add all files
    repo.git.add(all=True)
    
    # Create commit
    commit_message = f"Backup {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    repo.index.commit(commit_message)
    
    # Push to GitHub (replace with your GitHub repo URL)
    origin = repo.create_remote("origin", url="https://github.com/YOURNAME/clipvault-vault.git")
    origin.push()
    
    print("Backup complete! ✅")

if __name__ == "__main__":
    backup_to_github()