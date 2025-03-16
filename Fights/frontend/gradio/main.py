import gradio as gr

import sys, os
middleware_path = os.path.join(os.path.dirname(__file__), "..", "..", "middleware")
sys.path.append(os.path.abspath(middleware_path))
from api_fights import api_enemy as en

with gr.Blocks() as iface:
    with gr.Tab("Import File"):
        with gr.Group():
            input_file = gr.File(label="Upload File")
            file_output = gr.Textbox()
            input_file.change(en.process_file, input_file, file_output)
            input_checkbox = gr.Checkbox(label="Check")
            checkbox_output = gr.Textbox()
            input_checkbox.change(en.test, input_checkbox, checkbox_output)

    with gr.Tab("Checkbox"):
        input_checkbox = gr.Checkbox(label="Check")
        checkbox_output = gr.Textbox()
        input_checkbox.change(en.test, input_checkbox, checkbox_output)

# To-Do : Suppress share=True message
iface.launch()
