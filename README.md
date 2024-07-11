
# Project Title
This project is a web application that allows users to upload PDF files and receive concise summaries of their content. It leverages the Gemini LLM (Large Language Model) for generating summaries and uses Flask for deployment. The application processes the uploaded PDF, extracts the text, and uses the Gemini model to produce a summary, providing users with an easy way to understand large documents quickly.
## Technologies used 
->Gemini LLM: For generating summaries.
->Flask: For web application deployment.
->Python: Main programming language.
->PyPDF2: For PDF text extraction.
->HTML/CSS: For the web interface.
## Setup and installation
1. Clone the repository:
https://github.com/dishabarmola/Text-Summariser

2. Create a virtual environment and activate it:
python3 -m venv venv  
source venv/bin/activate


3. Install the required packages: 
Install all the required dependencies like flask, langchain etc.

4. Set up environment variables:
In the your_module.py edit your gemini API key and use the application.



## Usage
1. Run the flask application:

In terminal run "Python app.py"

2. Access the web application

Open your web browser and run into the local host http://127.0.0.1:5000.

3. Upload a PDF:
Click on the choose file to select a pdf and upload it.

4. Get the summary:
The application will process the pdf and generate  a concise summary that will show on the web interface.



 
