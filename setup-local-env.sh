if [ -f "env-local.env" ]; 
    then echo "export env-local.env" && export $(grep -v '^#' env-local.env | xargs); 
    else echo "need to locate a env-local.env";
fi