# Mini Project-Network Security

This repository contains a GitHub Actions workflow for scanning your codebase for potential security threats using ClamAV, an open-source antivirus engine.

## Overview

We created two seperated plugins for detecting malicious code in the repository we are about to pull/clone:
1. The security-scan.yml workflow is designed to run ClamAV on your repository to check for malicious files and report the results. This action is triggered on push and pull request events to the main branch.
2. The scan_repo.py script is designed to clone a specified GitHub repository, scan its contents for malicious code using YARA rules, and report any findings. After scanning, the script cleans up by removing the cloned repository directory.

## Setup

To use ClamAV plugin, follow the steps below:

**Clone this repository or create a new repository**:
   ```sh
   git clone https://github.com/<your-username>/<your-repo.git>
   cd <your-repo>
   mkdir -p .github/workflows
   cd .github/workflows

   [here copy the security-scan.yml file]

   git add .github/workflows/security-scan.yml
   git commit -m "Add security scan workflow"
   git push

To use YARA plugin, follow the steps below:






## Review 

The output of clamscan will be saved to scan.log, which will be available in the logs of the GitHub Actions run. You can review this log for detailed information on any malicious files found.

   

