© The Chancellor, Masters and Scholars of The University of Oxford. All rights reserved.

Scheduling a Python program to run daily in AWS

# Instructions

<details>
<summary>Step 1. Go to the AWS Console and type "Lambda" in the search bar</summary>

![Step 1](README_images/find_lambda.png)

***
</details>
<details>
<summary>Step 2. Press "Create a function"</summary>

![Step 2](README_images/create_a_function.png)

***
</details>
<details>
<summary>Step 3. Configure the function </summary>

Choose "Author from scratch", Python, and a name for your function (for example: daily_python_task)

![Step 3](README_images/function_params.png)

***
</details>
<details>
<summary>Step 4. Paste the code in the editor </summary>

![Step 4](README_images/code_editor.png)

***
</details>
<details>
<summary>Step 5. Press "Add trigger" </summary>

![Step 5](README_images/add_trigger.png)

***
</details>
<details>
<summary>Step 6. Set the source of the trigger </summary>

It should be EventBridge

![Step 6](README_images/trigger_source.png)

***
</details>
<details>
<summary>Step 7. Create the trigger rule</summary>

Give it a name (for example: daily_python_trigger), setup the Schedule Expression, for example cron(0 0 * * ? *) (runs daily at midnight UTC)

![Step 7](README_images/trigger_params.png)

***
</details>




