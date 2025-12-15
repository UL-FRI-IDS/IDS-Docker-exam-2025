# import libraries

FEATURE_COLUMNS = ['loan_amount', 'loan_interest_rate', 'loan_percent_income', 'age', 'income', 'years_work_experience', 'owns_home', 'credit_history_length_years', 'credit_score', 'previous_loan_defaults']
TARGET_COLUMN = "loan_approved"

# read CSV

X = df[FEATURE_COLUMNS]
y = df[TARGET_COLUMN]

# train test split (test size = 30%; random state = 1; shuffle = True)


# baseline

# random forest
