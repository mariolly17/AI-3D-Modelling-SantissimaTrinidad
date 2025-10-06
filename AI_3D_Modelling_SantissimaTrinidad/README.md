# AI 3D Modelling of Santísima Trinidad Church

This repository accompanies the article:
**"Validated Quantitative and Geometric Workflow for AI-Enabled 3D Reconstruction of Modernist Heritage"**
by Mariolly Dávila Cordido and Renata de Mendonça Espinheira Gomes.

## Repository Structure
- `/scripts/` – Python files for AHP analysis, geometric validation (Hausdorff, Chamfer, RMSE), and model export.
- `/models/` – Corrected CAD and parametric models (DXF, STL, OBJ).
- `/data/` – AHP matrices and digitized reference point sets derived from archival drawings.
- `/docs/` – Software versions, parameters, and usage instructions.

## Usage Example
```
python geometric_validation.py --ref reference.stl --model ai_model.obj --metric hausdorff
```

## License
Distributed under CC-BY 4.0 License.
