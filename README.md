# **InfiStorage**

A simple tool to upload images to GitHub, store metadata in Supabase, and manage everything seamlessly via a user-friendly GUI with drag-and-drop support.

---

## **Features**
- Upload images directly to a GitHub repository.
- Store metadata (title, description, image URL) in Supabase.
- Drag-and-drop support for easy image uploads.
- GUI built with Tkinter for simplicity and ease of use.

---

## **Prerequisites**
### **GitHub Setup**
1. Create a GitHub **Personal Access Token**:
   - Go to [GitHub Developer Settings](https://github.com/settings/tokens).
   - Generate a token with the following scopes:
     - `repo` (for private repositories).
     - `public_repo` (for public repositories).
   - Save the token for later use.

2. Create a GitHub repository to store images:
   - Example: `your_username/images_temp`.
   - Make sure you have write access to the repository.

---

### **Supabase Setup**
1. Create a Supabase project at [Supabase](https://supabase.io/).

2. Create a table in your Supabase project using the following SQL:

   ```sql
   CREATE TABLE images (
       id SERIAL PRIMARY KEY, -- Auto-incrementing unique identifier
       title TEXT NOT NULL, -- Title of the image
       description TEXT, -- Description of the image
       image_url TEXT NOT NULL, -- URL of the image hosted on GitHub
       uploaded_at TIMESTAMP DEFAULT NOW() -- Timestamp of when the image was uploaded
   );
   ```

3. Note down your **Supabase URL** and **Anon Key**:
   - Go to your Supabase project.
   - Navigate to **Settings** > **API**.
   - Copy the `API URL` and `Anon Key`.

---

## **Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/your_username/InfiStorage.git
cd InfiStorage
```

### **2. Install Requirements**
Make sure you have Python installed. Then, install the required dependencies:

```bash
pip install -r requirements.txt
```

### **3. Configure the Project**
Open the script and update the following variables:

#### GitHub Credentials:
```python
GITHUB_TOKEN = "your_github_personal_access_token"
GITHUB_REPO = "your_username/your_repo_name"
GITHUB_BRANCH = "main"
```

#### Supabase Credentials:
```python
SUPABASE_URL = "your_supabase_url"
SUPABASE_KEY = "your_supabase_anon_key"
```

---

## **Usage**

1. Run the application:
   ```bash
   python infistorage.py
   ```

2. Enter the image's **title** and **description** in the GUI.
3. Drag and drop the image file into the designated area, or use the **Browse File** button to upload the file.
4. The application will:
   - Upload the image to the specified GitHub repository.
   - Save the metadata (title, description, image URL) in the Supabase database.
5. A success or error message will appear upon completion.

---

## **Contributing**
Feel free to contribute to InfiStorage by submitting issues or pull requests. We welcome all feedback and improvements.
