import gradio as gr

import sys, os
middleware_path = os.path.join(os.path.dirname(__file__), "..", "..", "middleware")
sys.path.append(os.path.abspath(middleware_path))
from api_fights import api_enemy as en

iface = gr.Interface(
    fn=en.process_file,
    inputs=gr.File(label="Upload File"),
    outputs="text"
)

# To-Do : Suppress share=True message
iface.launch()
