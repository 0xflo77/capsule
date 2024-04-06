## SVG variant generator
- This script uses a straightforward strategy for selecting colors. Since there's a requirement for the base and top to always be darker than the eyelids, it ensures this by always selecting base/top colors from the darker half and eyelid colors from the lighter half.
- Each color from the list is used at least once, with the script rotating through all 80 colors.
- Luminace visual is a helper that generates html
