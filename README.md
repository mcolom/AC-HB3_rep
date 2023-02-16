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
* Should we use a real center-tap transformer, or a modern switching one? Switching regulators might introduce some periodic noise (ripple voltage) that could affect the video signal. Is this significant?
* How to build the connector? With a 3D printer? Any other alternatives?
* Are the 3 pins in the connector a known model available today? Which one? Otherwise, any alternative?

The final product should include the PCB with the components, a case, a 3-pin connector replacement, and a normal electric plug.

**Needless to say, any contributions are very welcome!**

# Contents
* diagram.py: it draws a diagram of the 3-pin connector, with the sizes and distances which are believed to be correct.

# Resources
* The Sony HB-F1XD service manual, including the detailed schematics at the end: https://archive.org/details/sonyhbf1xdsm/page/n21/mode/2up
* Two threads at MSX's MRC: https://www.msx.org/forum/msx-talk/hardware/sony-hb-f1-power-cord and  https://www.msx.org/forum/msx-talk/hardware/panasonic-fsaa51-power-adapter
* A similar project is available here at the MSX Village (French): https://www.msxvillage.fr/forum/topic.php?id=3345#m76611 However the it's only the circuit and it doesn't include the 3-pin connector.
* Educational Youtube video by Ben Eater on the principle used by switching PSUs to increase the voltage at the output: https://www.youtube.com/watch?v=4alV5LzHLE4

# Resources about the connector
* A 3D model by Jonn Blanchard is available here: https://www.myminifactory.com/fr/object/3d-print-panasonic-fs-a1-sony-hb-f1-neo-geo-cd-psu-connector-196715
* The RS's site lists many IEC connectors, but none of them is exactly the same as AC-HB3. https://uk.rs-online.com/web/c/connectors/mains-dc-power-connectors/iec-connectors/
* The Schurter's site also lists many IEC connectors, but again none of them seems to correspond to ours: https://www.schurter.com/en/search?searchText=%20iec&searchCategory=products
* Member "kifo" of the Conexión MSX Telegram group explains that for the pins inside the connector (using the model by Jonn Blanchard) Molex connectors may be used.
* In Digikey it's possible to find several connectors that might be a good fit: https://www.digikey.fr/fr/products/filter/contacts/multi-usage/336 Filtered to have only Molex: https://www.digikey.fr/fr/products/filter/contacts/multi-usage/336?s=N4IgjCBcpgnAHLKoDGUBmBDANgZwKYA0IA9lANogAMIAugL7EC0E0IakWeRpFIATAGY69UUA
