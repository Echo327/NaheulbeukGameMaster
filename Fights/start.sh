#!/bin/bash

# Functions

build() {
    python backend/resources/generate_jsons.py
}

clean() {
    rm -v backend/resources/*.json
    echo "All json files in resources have been deleted."
}

launch_gradio() {
    python frontend/gradio/main.py
}

launch_ipynb() {
    jupyter-notebook frontend/fights.ipynb
}

echo "Please make sure you have gradio installed (pip install --upgrade gradio)"
echo "or make sure you have jupyter-notebook installed (pip install --upgrade jupyter)"
echo "for the appropriate option to work"

echo "Possible options: build, clean, gradio, ipynb"

read -p "Enter the desired option: " user_input

case "$user_input" in
    "build")
        build
        ;;
    "clean")
        clean
        ;;
    "gradio")
        launch_gradio
        ;;
    "ipynb")
        launch_ipynb
        ;;
    *)
        echo "Error: Invalid input. Please enter either 'build', 'clean', 'gradio', or 'ipynb'."
        exit 1
        ;;
esac
