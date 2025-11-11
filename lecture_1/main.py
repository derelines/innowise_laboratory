# Import necessary components from the colorama library
# ('init' is a function to initialize colorama for cross-platform support;
#  'Fore' controls the foreground text color;
#  'Back' controls the background color;
#  'Style' controls additional styles)
from colorama import init, Fore, Back, Style

# Initialize colorama for cross-platform colored terminal output
init()

# Print colored Hello World
# Fore.RED sets the text color to red. Back.YELLOW sets the background to yellow
# Style.RESET_ALL resets all styles back to default after the text
print(f"{Fore.RED}{Back.YELLOW}Hello World{Style.RESET_ALL}")
# Fore.GREEN sets the text color to green
print(f"{Fore.GREEN}Hello World in Green!{Style.RESET_ALL}")
# Fore.BLUE sets the text color to blue. Style.BRIGHT makes the color brighter
print(f"{Fore.BLUE}{Style.BRIGHT}Hello World in Bright Blue!{Style.RESET_ALL}")
# Fore.MAGENTA sets the text color to magenta. Back.CYAN sets the background to cyan
print(f"{Fore.MAGENTA}{Back.CYAN}Hello World with Magenta text and Cyan background!{Style.RESET_ALL}")