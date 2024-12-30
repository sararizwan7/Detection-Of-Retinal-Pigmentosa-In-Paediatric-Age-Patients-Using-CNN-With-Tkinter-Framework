![CNN](https://media0.giphy.com/media/f9BBuAaHHgT47PwUh6/giphy.gif)

# _**Detection Of Retinal Pigmentosa In Paediatric Age Patients Using CNN With Tkinter Framework**_
Detection of retinal pigmentosa in paediatric age patients involves a combination of deep learning and MySQL in the process of registering the user who wants to use the application. The project consists of a Tkinter GUI where the user can register himself/herself and login to evaluate and test the model. The model predicts by taking image as an input an predicts whether a person is affected with retinal pigmentosa or not, the model which we use to train and test the data is Convolutional neural network model.

# _**Base Paper**_
+ https://www.researchgate.net/publication/342285658_Deep_Learning-Based_Detection_of_Pigment_Signs_for_Analysis_and_Diagnosis_of_Retinitis_Pigmentosa
+ https://www.researchgate.net/publication/327294998_Machine_Learning_and_Deep_Learning_approaches_for_Retinal_Disease_Diagnosis

# _**Algorithm Description**_
**Convolutional Neural Network:**
As we all are aware of the fact, how deep learning and transfer learning is revolutionizing the world with its immense capability of handling any kind of data and learning so efficiently. So, similarly we have applied the same concept by picking a deep learning model i.e., Convolutional neural network which basically work son the principle of having filters. Each convolutional layer has some specific filters to identify and extract the features from the input image and learn it and transfer it to other layers for further processing. We can have as many filters as possible in the convolutional layer depending on the data we are dealing on. Filter are nothing but feature detectors in the input data. Along with the convolutional layer we also have other layers which does further pre-processing such as Maxpooling, Activation function, Batch Normalization and dropout layer. These all contribute to the CNN model creation and along with the flatten and output layer. The reason we do flattening is to feed the output of the CNN model to the dense layer which gives us the probability of the predicted value.

![CNN](https://learnopencv.com/wp-content/uploads/2023/10/Convolutional-Neural-Network.png)

**Reference**

+ https://towardsdatascience.com/convolutional-neural-networks-explained-9cc5188c4939

# _**Installing SQLITE Database**_

It is integrated with database login support, we might need to install SQLite database in our system to make the code running. Trust me this will not take more than 5 min of your precious time, hang on.
1.	Download the SQLITE standard installer.
+ https://sqlitebrowser.org/dl/
2.	After the download has ended, click on the .msi file and follow the all the necessary installation procedures.
3.	Click on next and make sure to check the boxes for making the shortcuts.
4.	Click on next and the installation procedures begins.
5.	At last, click on finish to complete the setup procedure.


# _**How to Execute?**_
So, before execution we have some pre-requisites that we need to download or install i.e., anaconda environment, python and a code editor.
**Anaconda**: Anaconda is like a package of libraries and offers a great deal of information which allows a data engineer to create multiple environments and install required libraries easy and neat.

**Download link:**

![Anaconda](https://1.bp.blogspot.com/-UJ1Ws2zZ9V4/TtMbG2ynJiI/AAAAAAAABbM/m6t2kuEhKdY/s1600/The-biggest-anaconda-snake-3.jpg)

https://www.anaconda.com/

**Python**: Python is a most popular interpreter programming language, which is used in almost every field. Its syntax is very similar to English language and even children and learning it nowadays, due to its readability and easy syntax and large community of users to help you whenever you face any issues.

**Download link:**

![Python](https://i0.wp.com/reptileworldfacts.com/wp-content/uploads/2019/05/male-blonde-super-tiger-reticulated-python.jpg?resize=351%2C351&ssl=1)

https://www.python.org/downloads/

**Code editor**: Code editor is like a notepad for a programming language which allows user to write, run and execute program which we have written. Along with these some code editors also allows us to debug, which usually allows users to execute the code line by line and allows them to see where and how to solve the errors. But I personally feel visual code is very good to work with any programming language and makes a great deal of attachment with user.

**Download links:**

![Vs code](https://schwabencode.com/contents/logos/VS2019-Badge.png) ![Pycharm](https://i0.wp.com/scracked.com/wp-content/uploads/2020/01/PyCharm-2019.3.4-Crack.png?fit=200%2C200&ssl=1)

+ https://code.visualstudio.com/Download, 
+ https://www.jetbrains.com/pycharm/download/#section=windows

# _**How to create a new environment and configure jupyter notebook with it.**_
Let us define an environment and why we need different environments. An environment is a collection of libraries that are required to run our project. When we already have an environment with the necessary libraries, why do we need a new environment?
To avoid version mismatches, we create a new environment for each project. For example, in your previous project, you used "tf env" with tensorflow 2.4 and keras 2.4, but in your current project, you must use tensorflow 2.6 and keras 2.6. If you continue your project in the "tf env" environment, there will be a version mismatch and you will need to update tensorflow and keras, but this will cause problems with the previous project's execution. To avoid this, we create a new environment with tensorflow 2.6 and keras 2.6 and resume our project.

Let us now see how to create an environment in anaconda.
+ Type “conda create –n <<name_of_your_env>>”
example: conda create -n env
+ It will ask to proceed with the environment location, type ‘y’ and press enter.
+ When you press ‘y’, the environment will be created. To activate your environment type conda activate <<your_env_name>> . E.g., conda activate myenv.
+ You can see that the environment got changed after conda activate myenv line. It changed from “base” to “myenv” which means you are now working in “myenv” environment.
+ To install a library in your virtual environment type pip install <library_name>.
e.g., pip install pandas
+ Instead of installing libraries one by one you can even install by bunch, i.e., we have a txt file called requirements.tx which consists of all the libraries required to proceed with the project, so we can use it.
+ so, before installing requirements.txt, make sure you are in the specific path where your requirements.txt is located, basically this file is located in the folder where our executable files are located, so we need to move to that directory by following command.
**cd C:\folder_name**
+ Here A -> drive, folder name -> path where your executable file is saved
+ I go to that file path in anaconda using cd command 
1.	Go to drive where your project file is.
2.	Go to the path of your project using cd <path>
3.	Type pip install –r requirements.txt 
+ And all your required libraries will be downloaded and you can start your project.
+ But if you want to use jupyter notebook on the new environment you have to set it up for the new environment.
+ After you have installed all the libraries and created an environment, you need an editor to run the code, that is starting jupyter notebook, as soon as you enter jupyter notebook in the terminal you will definitely get this error. “Jupiter” is not recognized as an internal or external command.
So, to solve it it we have 2 commands.
1.	conda install –c conda-forge jupyterlab
2.	conda install –c anaconda python
Now you are ready to use jupyter on this environment and start with your project!

![thanks](https://media1.tenor.com/images/11ae4fcfc41bb9e66a0176fcfc38e695/tenor.gif?itemid=8486985)
  
  
# _**Steps to execute**_
**Note:** Make sure you have added path while installing the software’s.

1.	Install the prerequisites/software’s required to execute the code.
2.	Press windows key and type in anaconda prompt a terminal opens up.
3.	Before executing the code, we need to create a specific environment which allows us to install the required libraries necessary for our project.
•	Type conda create -name “env_name”, e.g.: conda create -name project_1
•	Type conda activate “env_name, e.g.: conda activate project_1
4.	Make sure you are in the correct path in your terminal, where you have saved your executable file/folder. E.g.: cd A:\project\AI\Completed\project_name, then press enter.
5.	Install necessary libraries from requirements.txt file provided.
6.	Run pip install -r requirements.txt or conda install requirements.txt (Requirements.txt is a text file consisting of all the necessary libraries required for executing this python file. If it gives any error while installing libraries, you might need to install them individually.)
7.	Unzip All .rar Files.
8.	Run main.py in your anaconda terminal and make sure to change the path where your executable files are located in the anaconda terminal.

# _**Data Description**_
The dataset was downloaded from a private data repository which might not be available now. The dataset is divided into train and test sets, where each folder is again divided into negative and positive folders, where thee training_negative consists of 386 images and training_positive consists of 134 images, similarly test_negative consists of 96 images and test_positive consists of 34 images. Shape of all the images is equally scaled about 3072 x 2048‬.‬‬

**Negative**

![Negative](https://www.washingtoneye.com/wp-content/uploads/2021/12/retina-iStock-172711954.jpg)

**Positive**

![Positive](https://www.verywellhealth.com/thmb/urvJI_6CanHUX6Ig5LNuruQbM4M=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-308783-003-56acdcd85f9b58b7d00ac8e8.jpg)

# _**Evaluation Metrics**_

Evaluation metrics are considered as one of the most important steps in any machine learning and deep learning projects, where it will allow us to evaluate how good our model is performing on the new data or on unseen data. There are a lot of evaluation metrics which can be used in order to assess how good our model is performing, in our case, since we are dealing with binary classification and neural network, we are going to sue binary_cross_entropy/log_loss, which basically compares the actual class with the predicted probabilities and then it calculates a corrected probability by subtracting it with the probability of a datapoint belonging to class1 with the predicted probability, i.e. for the case of ID8 it is actually class 0, but the probability is of class 1 is 0.56, so we subtract (1 – 0.56), we get 0.44 that is our corrected probability.  Then Log_loss is calculated by applying log transformation on each of the calculated_probablities. The the average of the negative corrected_probablities are taken which will gives us the log_loss/binary_cross_entropy, the lower the value the better our model is performing. 

# _**Issues Faced.**_
1. We might face an issue while installing specific libraries.
2. Make sure you have the latest version of python or 3.8, since sometimes it might cause version mismatch.
3. Adding path to environment variables in order to run python files and anaconda environment in code editor, specifically in visual studio code.

# _**Note:**_
**All the required data hasn't been provided over here. Please feel free to contact me for any issues. You can also download the dataset from the given link below.**

### _**Let’s Connect**_
<a href="https://linkedin.com/in/mudassiruddin21" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/linkedin.svg" alt="mudassiruddin21" height="30" width="40" /></a>

![Connect](https://media2.giphy.com/media/l1O6zvqu7O317887HF/source.gif)

# _**Yes, you now have more knowledge than yesterday, Keep Going.**_
![Happy](https://media.giphy.com/media/GK7grZYLG7cs0/giphy.gif)
  
