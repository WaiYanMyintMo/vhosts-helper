# Welcome to vhosts-helper
This program is designed to help you
* Edit Hosts File
* Edit Vhosts File

Key features are -
* Basic Templating Engine
* Extensive Customization
### Intro
By default, both hosts and vhosts are edited together (configurable)

Hosts edit -  Program edit hosts file and add some data. Example: '127.0.0.1 example.com' is appended to the end of file. (configurable)

Vhosts edit - Program edit apache vhosts file and add some data. Example:

'<vhosts\>

sitename = Example.com

DocumentRoot = 'D:\Document\Root'

...

<vhosts\\>'

You can configure the path to these files in **Config**

## Installation
Download latest release from https://github.com/Stiles-X/vhosts-helper/releases
## Usage
Extract the downloaded folder if zipped file.

Next, go inside the 'app' folder.

Run main.exe / main.py as administrator
//There is one command line argument, and it is for path of config.yaml

**NOTE:** You might want to configure your inputs in config first, read **Config** section below
## Config
You have to edit config in order to change  your inputs.


To get to the config file, first go the the config folder.

Next, open config.yaml in a text editor to start editing.


You should know that config.yaml is broken up into 3 groups
* keyword_config
* editor_config
* template_config
### Basic Configuration
*In editor_config:*

**Find** "ServerName" : "Example1.com"

You have to change *Example1.com* to what ever address you would like. Example: "examplewebsite.com"


**Find** "DocumentRoot": 'D:\Example1'

You have to change D:\Exmaple1 to your website project's root folder's full path. Example: "C:\\Users\\Username\\YourWebsite\\DocumentRoot"


Next, you may have to change **port number** to 8080 or 8090, etc.


*In keyword_config:*

**Find** "PortNumber1": '80'
You have to change 80 to another port number. Example: '8080', '8090'
*Note: PortNumber1 is a default template keyword, this can be changed as in **Template** section below *

### Intermediate Configurations
This section assumes more familiarity with computers and will shorten the description for each setting

*In editor_config:*


  **HostsPath**: 'Path\To\Host' Example: 'C:\Windows\System32\drivers\etc\hosts'
  
  
  **VhostsPath**: 'Path\To\Vhost' Example: 'C:\xampp\apache\conf\extra\httpd-vhosts.conf'
  
  
  **EditIncludes**: 'Both' Example: 'Hosts', 'Vhosts' or 'Both'
  This setting determines either Hosts or Vhosts or Both is edited.
  
  
  *In template_config:*
  
  **EditType** : 'append' Example: 'this string is matched'
  
  **EditOption** : '-' Example: '+'
 
  These 2 are a little bit harder to understand because EditOption depends on EditType. I'll explain.
  
  
  EditType has two types - 'append' type and 'string matching' type.
  
  
  In append type, data is appended to either the top, or bottom of the file.
  
  You can choose top or bottom with EditOption '+' and '-' respectively.
  
  
  In 'string matching' type, the program looks through the file for 'this string is matched' and insert data there.
  
  You can choose either above the matched string or below with EditOption '+' and '-' respectively.
  
  If string is not found it will behave as if you chose 'append' type instead. Meaning if EditOption was '+', the data will be inserted at the top of the file.
  ### META CONFIGURATIONS
  Hey, I tried as much as possible to put all configurations in the config file. The ONLY hard-coded one is config_path, which is needed to find the config file. You can change it in configurer.py file if you are using the python version. If you are using an e

 Don't be sad.... It is available as a command line argument!
 
  main.exe PATH\TO\CONFIG.YAML and that's it! Relative path is supported.
  ### Uninportant Configurations
  *In editor_config:*
  
  **SavesToOutput**: 'True' Example: 'False'
  
  This setting determines if you want a copy of your data in a text file in Output folder.
  
  
  **OutputPath**: '\.\.\Output\'  Example:'Path\To\Output'
  This setting determines where the output file is saved.
  
  **Note:** Output is overwritten if ServerName is the same.

## Template

The program features a very basic templating engine. Here's how it works

* You have a template file, with keywords.
* You tell the program what keywords you used, and what values to replace it with
* Program replace the keywords with the value

You have to set your keywords and value in config.yaml file.

*In keyword_config:*

**Example_Keyword**: 'Example Value'
### Set Template Path
*In template_config:*

  **HostsTemplatePath**: '\.\.\Config\hosts_template.txt' Example: 'Path\To\Template.txt'
  
  
  **VhostsTemplatePath**: '\.\.\Config\vhosts_template.txt' Example: 'Path\To\Template.txt'
  
  
#### Practical Example

* Find Template (template.txt) using Template_Path (path\to\template)
* Read content of Template (My name is Name01)
* Get Keyword Config using keyword_config from config.yaml.
* Read content of Keyword Config (Name01: 'John')
* Replace Template using Keyword Config
* Read content of replaced Template (My name is John)
* Write content to somewhere

### Bonus Feature
There is a bonus feature I have included.

In keyword_config:

I can put a $ sign (Name01: '$ServerName')

What it does is that, instead of writing (My name is $ServerName), it writes (My name is Example1.com).

What happened? By using $ sign, you are telling it to -
* go to editor_config
* find 'ServerName' (without the $) on the left column
* use the value of ServerName (Example1.com) instead.
## Footnote
I see you are reading this. That means you have read through all the features of this program. I also urge you to read config.yaml file's comments as there are more concise, incomplete, and badly worded examples and explanations.

Please ask me for more features, or tell me about problems you have. I will fix them all, depending on conditions. Thank you

## FAQ (Frequently Asked Questions)
**Will this be available on PyPi?**

-If anyone makes a request, yes. I will have to remove print statements and make it more module like than app like. I don't know how I will maintain both versions at once.

**How can I help contribute? (with documentation, faq, code, guidance, etc.)**
-Please contact me through github or some sort.
