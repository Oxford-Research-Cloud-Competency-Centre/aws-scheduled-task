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
<summary>Step 5. Add dependencies </summary>

When we import a Python module, for example 'import requests', we need to provide a layer that includes this module. 

Press "Add layer"

![Step 5](README_images/add_layer.png)

Choose "AWSSDKPandas-Python313"

![Step 5](README_images/layer_params.png)

If you change the code and add custom modules, you might need to create a .zip file and a custom layer 

***
</details>
<details>
<summary>Step 6. Adjust timeout </summary>

Change the default timeout (3 seconds) to a reasonable value (1 minute) 

![Step 6](README_images/timeout.png)

***
</details>

## Scheduling

<details>
<summary>Step 1. Press "Add trigger" </summary>

![Step 1](README_images/add_trigger.png)

***
</details>
<details>
<summary>Step 2. Set the source of the trigger </summary>

It should be EventBridge

![Step 2](README_images/trigger_source.png)

***
</details>
<details>
<summary>Step 3. Create the trigger rule</summary>

Give it a name (for example: daily_python_trigger), setup the Schedule Expression, for example cron(0 0 * * ? *) (runs daily at midnight UTC)

![Step 3](README_images/trigger_params.png)

***
</details>




