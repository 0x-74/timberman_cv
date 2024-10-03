# How to Run This

Follow these steps to get the Timberman script running on your MacBook:

1. **Download Timberman**: 
   - Install the Timberman game from the App Store on your MacBook.

2. **Select Character**:
   - Choose the "Mexico Guy" from the menu. *(Note: Currently, this script only supports the Mexico Guy due to the use of template matching and not a trained model.)*

3. **Download the Script**:
   - Download the Python file named `main.py`.

4. **Install Dependencies**:
   - Open your terminal and navigate to the directory where `main.py` is located.
   - Run the following command to install the required packages:
     ```bash
     pip install -r requirements.txt
     ```

5. **Run the Script**:
   - Execute the script using one of the following commands:
     - If you’re using `sudo`:
       ```bash
       sudo python3 main.py
       ```
     - If you are in a virtual environment:
       ```bash
       sudo python main.py
       ```

6. **Stopping the Script**:
   - You can stop the execution of the script by pressing the `Escape` key. *(Note: This may not work if you did not use `sudo`.)*

## Side Note

- **Model Limitations**: 
  - The current model may fail occasionally, depending on the side from which obstacles appear. This limitation arises from using confidence levels instead of detection positions. A fix for this issue is planned for future updates.
