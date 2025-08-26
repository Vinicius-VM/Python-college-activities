#install.packages('reticulate')
#reticulate::install_miniconda()

library(reticulate)
py_require("jax")    # Declare jax is a requirement

jax <- import("jax") # <-- initialize Python with declared requirements
