#install.packages('reticulate')
#reticulate::install_miniconda()

#library(reticulate)

# create a new environment
#virtualenv_create("r-reticulate")

# install SciPy
#virtualenv_install("r-reticulate", "scipy")

# import SciPy (it will be automatically discovered in "r-reticulate")
#scipy <- import("scipy")

# indicate that we want to use a specific virtualenv
#use_virtualenv("r-reticulate")

# import SciPy (will use "r-reticulate" as per call to use_virtualenv)
#scipy <- import("scipy")

##Achei util para os códigos acima:
#https://rstudio.github.io/reticulate/articles/python_packages.html