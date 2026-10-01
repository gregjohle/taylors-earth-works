import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Hauling & Trenching removals from headers and meta
content = content.replace(', tractor, skid steer, and dump truck hauling services.', ', tractor, and skid steer services.')
content = content.replace('skid steer services, tractor work, dump truck hauling,', 'skid steer services, tractor work,')
content = content.replace('tractor, and dump truck earthworks', 'and tractor earthworks')
content = content.replace('land clearing, and dump truck hauling in Zebulon', 'and land clearing in Zebulon')

# Schema changes
content = content.replace('"name": "Dump Truck Material Hauling"', '"name": "Land Clearing"')
content = content.replace('"name": "Skid Steer & Tractor Work"', '"name": "Grading & Excavating Services"')

# 2. Insurance
content = content.replace('Owner-Operated • Zebulon, NC • Fully Insured', 'Owner-Operated • Zebulon, NC • Workers Comp & General Liability')
content = content.replace('Licensed &amp; Fully Insured Contractor', 'Workers Comp &amp; General Liability')

# 5. Skid steer rename
content = content.replace('<h3 class="service-title">Skid Steer &amp; Tractor Work</h3>', '<h3 class="service-title">Grading &amp; Excavating Services</h3>')

# 6. Transparent estimates
content = content.replace('<p>Itemized quotes covering material tonnage, machine hours, and timeline with zero surprises.</p>', '<p>You get an accurate, fair priced estimate for all of your project needs.</p>')

# 7. Equipment fleet removal
equipment_block = """          <div class="equipment-badge-card">
            <h3>Our Equipment Fleet</h3>
            <p style="color: #cbd5e1; margin-bottom: 1.5rem; font-size: 0.95rem;">
              Having our own dump truck, tractor, and skid steer means faster turnaround times and lower costs since we never have to wait on rental yards or outside haulers.
            </p>
            <ul class="equipment-list">
              <li>
                <svg fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
                <div><strong>High-Capacity Skid Steer:</strong> 84" smooth grading bucket, tooth bucket &amp; heavy grapple.</div>
              </li>
              <li>
                <svg fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
                <div><strong>Heavy Utility Tractor:</strong> Hydraulic box blade with rippers for deep leveling.</div>
              </li>
              <li>
                <svg fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
                <div><strong>Heavy Tandem Dump Truck:</strong> Hauls up to 15 tons of crushed rock or soil per load.</div>
              </li>
              <li>
                <svg fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
                <div><strong>Dual-Slope Rotary Laser:</strong> Micro-accurate slope verification for concrete slabs.</div>
              </li>
            </ul>
          </div>"""
content = content.replace(equipment_block, '')

# 8. Services after footings
content = content.replace('precision clearing, grading, excavating, and footings.', 'precision clearing, grading, excavating, and footing services.')

# 10. Facebook text
content = content.replace('<p>Watch short video clips of the skid steer in action, see weekly before/after photos, and read real customer reviews.</p>', '<p>See weekly before/after photos, and read real customer reviews.</p>')

# Footer fixes
content = content.replace('<li><a href="#services">Dump Truck Hauling</a></li>', '<li><a href="#services">Land Clearing</a></li>')
content = content.replace('<li><a href="#services">Culverts &amp; Trenching</a></li>', '<li><a href="#services">Excavating Services</a></li>')

# Form fixes
content = content.replace('<option value="Skid Steer / Tractor Work">Skid Steer / Tractor Work</option>', '<option value="Grading & Excavating Services">Grading &amp; Excavating Services</option>')
content = content.replace('<option value="Dump Truck Hauling">Dump Truck Material Hauling</option>', '<option value="Land Clearing">Land Clearing</option>')
content = content.replace('<option value="Trenching & Culverts">Trenching &amp; Culvert Pipes</option>', '<option value="Excavating Services">Excavating Services</option>')


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
