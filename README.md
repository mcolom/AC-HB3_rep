# AC-HB3 replacement
This is a project to design a replacement for the Sony's AC-HB3 MSX's PSU used in the HB-F1 and HB-F1II computers.  
The connector is proprietary (probably some sort of Mini-IEC), and it was also used in the Neo Geo CD and the HP SDD018-1000 PSU.  
There's a discussion thread here at MRC: https://www.msx.org/forum/msx-talk/hardware/brainstorming-to-design-ac-hbx-power-supplies

An schematic of the circuit is available at https://www.msx.org/wiki/Sony_AC-HB3 and it's quite simple: it consists on a center-tap transformer which provides 18 V AC, and also rectified 9 V. The input voltage 100 V, the standard Japanese. Building an alternative which can be plugged to 220 V would be useful for European users.

The design considerations and open questions are so far the following:

* Safety: it should be completely safe, and not to arc and set everything on fire, or electrocute anyone!
* Safety: some transformers come with the notice _"This product can expose you to chemicals including Di(2-ethylhexyl)phthalate (DEHP) which is known to the State of California to cause cancer"_. Obviously, these should be avoided. Question: do other modern transformers have DEHP or similar and we could be unaware of?
* Safety: we should include a fuse
* Quality: we should include a power regulator
* Should we use a real center-tap transformer, or a modern switching one? Switching regulators might introduce some periodic noise that could affect the video signal. Is this significant?
* How to build the connector? With a 3D printer? Any other alternatives?
* Are the 3 pins in the connector a known model available today? Which one? Otherwise, any alternative?

The final product should include the PCB with the components, a case, a 3-pin connector replacement, and a normal electric plug.

# Resources
* A 3D model by Jonn Blanchard is available here: https://www.myminifactory.com/fr/object/3d-print-panasonic-fs-a1-sony-hb-f1-neo-geo-cd-psu-connector-196715
* A similar project is available here at the MSX Village (French): https://www.msxvillage.fr/forum/topic.php?id=3345#m76611 However the it's only the circuit and it doesn't include the 3-pin connector.
