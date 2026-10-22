Mission: Build a "Smartphone" Blueprint
You just got hired to code the inventory system for a tech simulator game. Your job is to create a base Smartphone class, and then use Inheritance to create a special GamingPhone class.

Part 1: The Base Class (Smartphone)
Create a class called Smartphone with:

__init__ method that takes brand and model as inputs:

Set self.brand = brand

Set self.model = model

Set self.battery = 100 (Every phone automatically starts at 100% battery—don't ask the user for it in the inputs!).

use_app(self, app_name, battery_drain) method:

Check if self.battery is greater than or equal to battery_drain.

If it is, subtract battery_drain from self.battery and print: Using [app_name]... Battery at [self.battery]%

Otherwise (else), print: Battery too low to open [app_name]! Charge your phone.

charge(self) method:

Reset self.battery back to 100 and print: [self.model] is fully charged to 100%!


Part 2: The Boss Level — Inheritance (GamingPhone)

Create a child class called GamingPhone that inherits from Smartphone:

Give it a method called activate_turbo_mode(self):

It should print: 🚀 Turbo fan spinning on [self.model]! FPS boosted!

And it should drain 15 battery from self.battery.