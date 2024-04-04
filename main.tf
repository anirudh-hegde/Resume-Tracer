resource "null_resource" "resume_streamlit_resource" {
  triggers = {
    always_run = timestamp()
  }

  provisioner "local-exec" {
    command = "python3 -m streamlit run goat.py"
  }
}