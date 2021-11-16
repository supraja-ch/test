
## How do I run this project locally?
## APIs for reading xlsx file return json format with requesting inputs

### 1. Clone the repository:

    git clone https://github.com/supraja-ch/test.git

### 2. install requiremts.txt
     pip install -r requirments.txt
     
### 3. Run the server:
    python test.py

### 4. And open 127.0.0.1:5000/
  1. http://127.0.0.1:5000/readfile?input_id=3   ### send parameter "input" and pass file in form-data with parameter "inputfile"
  2. http://127.0.0.1:5000/search_readfile       ### send form-data parameter "inputfile" and "input_search"  json format
  
