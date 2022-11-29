# The Fitness Lab

## Flake8 Linting Errors
* All linting errors returned by flake8 were fixed to ensure that the code was written to the *** python standard.
* Linting errors within <code>.vscode/arctictern.py</code> as this was predefined code and in the <code>migrations</code> folders in all apps were ignored as this was system generated code.
* An error in the <code>checkout/apps.py</code> file saying that <code>'checkout.signals' imported but unused</code>. However, this is imported during runtime and is used within other files, therefore this error was ignored.
