# RUNBOOK.md
Steps to reproduce the validation process:

1. Install dependencies: `pip install open3d numpy`
2. Place reference and AI models in `/models/`.
3. Run geometric validation:
   ```bash
   python scripts/geometric_validation.py --ref models/reference.ply --model models/ai_model.ply
   ```
4. To perform AHP weighting:
   ```bash
   python scripts/ahp_analysis.py
   ```
