SELECT
    approp.row_number,
    approp.budget_authority_available_cpe,
    sf.amount as sf_133_amount
FROM appropriation as approp
    INNER JOIN sf_133 as sf ON approp.tas = sf.tas
    INNER JOIN submission as sub ON approp.submission_id = sub.submission_id AND
        sf.period = sub.reporting_fiscal_period AND
        sf.fiscal_year = sub.reporting_fiscal_year
WHERE approp.submission_id = {} AND
    sf.line = 1910 AND
    approp.budget_authority_available_cpe <> sf.amount