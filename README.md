<a name="readme-top"></a>


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Open Retrieval Augmented Generation</h3>

  <p align="center">
    A simple shell-based tool that you can customize for any application.
    <br />
    <a href="https://NVTEI.org">Visit the Organization</a>
    ·
    <a href="https://github.com/Rohit-K814307/open_rag/issues">Report a Bug</a>
  </p>
</div>

## MAJOR UPDATE - Google Collaboratory Support

This tool has been put entirely into a Google Collaboratory notebook available at [https://ai-training.nvtei.org](https://ai-training.nvtei.org). Please use this to run and access the RAG-pipeline detailed in this codebase. 


<!-- ABOUT THE PROJECT -->
## About The Project
<p align="center">
  <img src="https://blog.verisign.com/wp-content/uploads/VRSN_CompanyBrandedEmail_BlogImage8_201712-670x446.png" />
</p>

A local Retrieval Augmented Generation method to complete any tasks. This specific implementation is built for accelerating email writing using previously written emails. A couple of changes and this can be suitable for any task!

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites


#### WSL - Windows ONLY
This software runs on Linux/Mac - run it on Windows with Windows Subsystem for Linux (WSL).

Install WSL by running the following in Powershell:
```
wsl --install
```
Run standard WSL setup.

#### Ollama
Download [Ollama](https://ollama.com/) based on your system:


##### Windows w/ WSL or Linux
Open the Linux Comand Line and run the following: 
```
curl -fsSL https://ollama.com/install.sh | sh
```

##### MacOS
Download Ollama from this [link](https://ollama.com/download/mac) and run normal setup.

#### Anaconda
Install Anaconda within WSL, on Linux, or on Mac.

* Install Anaconda on WSL by following this [link](https://gist.github.com/kauffmanes/5e74916617f9993bc3479f401dfec7da).
* Use the Anaconda webpage [here](https://www.anaconda.com/) for all other systems


#### Outlook

Please install Outlook on your machine by following this link 

* Mac: [Outlook Installation](https://www.microsoft.com/en-us/microsoft-365/outlook/outlook-for-mac)

* Windows: Install directly from Windows Store

### Installation

_Follow these steps in order to set up the repo._

1. Clone the Repo
   ```sh
   git clone https://github.com/Rohit-K814307/open_rag/tree/windows
   ```
2. Change Directory and Install Conda Environment
   ```sh
    cd open_rag

    conda env create -f environment.yml
   ```
3. Get Outlook Email CSV

    i) Check this webpage for more specific instructions on getting [email CSV](https://techcommunity.microsoft.com/t5/excel/how-to-export-outlook-emails-to-excel-csv-file/m-p/3567227) from Outlook app 

    - Confirm that you are using the "old" Outlook app

    ii) Save to `./open_rag/data/raw.CSV`

4. Set up Ollama Model

    i) In a separate instance of the same terminal, run
    ```sh
    ollama serve
    ```
    ii) Create the Ollama custom model
    ```sh
    ollama create email_model_qwen -f ./email_model_qwen.txt 
    ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

This project is an LLM-powered client. 

In order to run the client, please follow these steps:

1. Open a new terminal at root
2. Allow running the generation script
    ```sh
    chmod +x ./open_rag/scripts/generate.sh
    ```
3. Query the LLM with your desired inputs and choose model parameters
    ```sh
    bash ./open_rag/scripts/generate.sh -q <query> -c <full path to csv emails> -e <your email address> ...
    ```
    - run `./open_rag/scripts/generate.sh -h` for help with arguments

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Rohit Kulkarni - "kulkarni.rohitva@gmail.com"

Link to [NVTEI](https://nvtei.webflow.io) Organization main page: 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

This project is presented to communities through the Northern Virginia Technology Education Initiative (NVTEI).


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: https://blog.verisign.com/wp-content/uploads/VRSN_CompanyBrandedEmail_BlogImage8_201712-670x446.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
