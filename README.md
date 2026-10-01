# Taylor's Earth Works - Contractor Website

A high-converting, lightning-fast, 100% free-to-host static website built specifically for an excavation, site prep, and grading business.

## Highlights
- **100% Free Hosting Forever:** Runs seamlessly on **Cloudflare Pages** or **GitHub Pages** with free SSL certificates and DDoS protection. Your friend only pays for the custom domain (~$10–$12/year).
- **Zero-Cost Contact Form:** Built-in form handling powered by **FormSubmit.co** (or Web3Forms). Quote requests arrive instantly in his email inbox with zero server costs, zero backend code, and built-in anti-spam protection.
- **Interactive Before & After Slider:** Interactive touch and mouse comparison slider showing the quality of site prep work before vs. after.
- **Mobile-First & Sticky Call Bar:** Over 70% of contractor leads come from mobile phones. Includes a persistent "Call Now" and "Get Estimate" bottom bar on mobile screens.
- **Contractor-Tailored Services:** Garage floor prep, driveway grading, land leveling, skid steer work, tractor box blading, and dump truck material hauling.
- **Facebook Integration:** Direct call-to-actions linking potential clients to his Facebook page for real-time project updates and social proof.
- **Engineered for Local SEO:** Clean semantic HTML5, fast load times (no bloated frameworks or CDN dependencies), and structured JSON-LD `LocalBusiness` schema for Google Maps ranking.

---

## 🚀 Quick Setup & Customization (5 Minutes)

### Step 1: Customize Business Information in `index.html`
Open `index.html` in any text editor and search for these placeholders:
1. **Phone Number:** Search for `5551234567` and replace with his actual phone number (e.g. `(555) 867-5309`).
2. **Email Address for Form:** The form is already set to route submissions to `taylorsearthworks@gmail.com`.
   > **Note on Form Activation:** The first time someone submits the form, FormSubmit sends a 1-click confirmation email to `taylorsearthworks@gmail.com` to verify ownership. Click the link once, and all future quote requests go straight to his inbox!
3. **Facebook Link:** Search for `https://www.facebook.com/your-facebook-page` and replace with his actual Facebook page URL.
4. **Service Area & Towns:** Search for `[Your City, County & Surrounding Areas]` and the list of town tags under `#service-area` to put his real local towns and counties.

### Step 2: Project Before & After Photos
The interactive comparison slider is already active and displaying his real project photos:
- `images/Before.jpg`: Rough, uneven clay subgrade inside building foundation walls.
- `images/After.jpg`: Laser-leveled, compacted stone base with vapor barrier ready for concrete.
*(To change or add more photos in the future, just drop new images into `images/` and update the filenames in `index.html`).*

---

## 🌐 How to Host for $0/Month (Zero Cost Forever)

### Option A: Cloudflare Pages (Recommended - Easiest & Fastest)
1. **Buy Domain:** Go to [Cloudflare Registrar](https://www.cloudflare.com/products/registrar/) or [Namecheap](https://www.namecheap.com/) and purchase his business domain (e.g., `taylorsearthworks.com` for ~$10/year).
2. **Create Free Cloudflare Account:** Go to [cloudflare.com](https://cloudflare.com) (free plan).
3. **Deploy Site:**
   - In Cloudflare Dashboard, go to **Workers & Pages** &rarr; **Create application** &rarr; **Pages** &rarr; **Upload assets**.
   - Drag and drop this folder (`Taylor's Earth Works`).
   - Click **Deploy Site**. In 10 seconds, the site will be live!
4. **Connect Custom Domain:**
   - In Cloudflare Pages, click **Custom Domains** &rarr; **Set up a custom domain**.
   - Type in `taylorsearthworks.com`. Cloudflare automatically provisions the free SSL certificate, DNS records, and HTTPS redirect.

### Option B: GitHub Pages (100% Free Alternative)
1. Create a free account at [github.com](https://github.com).
2. Create a new repository named `taylors-earth-works`.
3. Upload the project files (`index.html`, `styles.css`, `script.js`, and `images/`).
4. In repo settings &rarr; **Pages** &rarr; select `main` branch and click **Save**.
5. Under **Custom domain**, enter his domain name and follow the DNS CNAME instructions.

---

## 📁 File Structure
```
Taylor's Earth Works/
├── index.html                 # Main website page with SEO metadata and schema
├── styles.css                 # Rugged, modern contractor styling (responsive)
├── script.js                  # Slider drag/touch logic, mobile menu, and AJAX form handler
├── images/
│   ├── before-driveway.svg   # Placeholder graphic for 'Before' state
│   └── after-driveway.svg    # Placeholder graphic for 'After' state
└── README.md                  # This guide
```
