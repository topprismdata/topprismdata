# Maintaining the TopPrism profile

The profile homepage is a published view over a small, reviewable registry. The repository does not contain private brand-guide boards, customer data or publishing credentials.

## Change the featured projects

1. Edit [`portfolio/portfolio.yml`](../portfolio/portfolio.yml).
2. Keep `portfolio_status: flagship` and `pin: true` aligned for the projects intended for the homepage and GitHub Pins.
3. Keep at most six `pin: true` entries and at least one flagship in each homepage pillar.
4. Run the renderer and validators:

   ```bash
   python3 -m pip install -r requirements.txt
   python3 scripts/render_profile.py --write
   python3 scripts/render_profile.py --check
   python3 scripts/validate_profile.py
   ```

5. Review the generated English and Chinese pages together. Do not edit a generated block by hand.

The registry is not an automatic ranking. A change to the flagship set requires explicit human review; Stars, commit activity and recency are not promotion signals.

## Keep GitHub Pins synchronized

GitHub profile Pins are account-level UI state. They are deliberately not mutated by this repository or its workflow. After a reviewed change is merged, the account owner updates the Pins in the GitHub profile UI and then runs:

```bash
python3 scripts/report_pin_drift.py
```

Use `--strict` in a release check when drift should fail the check. A drift report is informational by default because the profile owner must perform the final UI action.

## Brand assets

The source brand-guide SVG boards stay in the private brand workspace. Only compact, derived assets are published under [`assets/brand`](../assets/brand). The public repository uses system font stacks and vector paths; it does not redistribute proprietary font files or private design boards.

## Publishing metadata

The profile repository description, homepage and topics are account metadata. Update them only after the content change has passed review. Never place a GitHub key, token or personal local path in a commit, issue, pull request or workflow log.
