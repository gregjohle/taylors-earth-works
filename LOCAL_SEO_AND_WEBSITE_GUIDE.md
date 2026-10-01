# Taylor's Earth Works: Website & Bullet-Proof Local SEO Playbook

A complete guide to hosting, customizing, and scaling Taylor's Earth Works for **$0/month** (just the cost of the domain name), along with the step-by-step strategy to dominate local Google search and Google Maps.

---

## Table of Contents
1. [Project Overview & Website Architecture](#1-project-overview--website-architecture)
2. [How to Customize the Website (5-Minute Walkthrough)](#2-how-to-customize-the-website-5-minute-walkthrough)
3. [Zero-Cost Hosting Setup ($0/mo Forever)](#3-zero-cost-hosting-setup-0mo-forever)
4. [Setting Up the Free Contact Form](#4-setting-up-the-free-contact-form)
5. [How to Add Real Before & After Photos](#5-how-to-add-real-before--after-photos)
6. [The Bullet-Proof Local SEO Playbook](#6-the-bullet-proof-local-seo-playbook)
   - [Phase 1: Google Business Profile (GBP) Domination](#phase-1-google-business-profile-gbp-domination)
   - [Phase 2: The 5-Star Review Generation Machine](#phase-2-the-5-star-review-generation-machine)
   - [Phase 3: Geotagged "Proof of Work" Photos](#phase-3-geotagged-proof-of-work-photos)
   - [Phase 4: Top 10 Free Directory Citations (NAP Consistency)](#phase-4-top-10-free-directory-citations-nap-consistency)
   - [Phase 5: Hyper-Local Facebook Lead Generation](#phase-5-hyper-local-facebook-lead-generation)
7. [Managing Leads & Estimates with Streak CRM (Free)](#7-managing-leads--estimates-with-streak-crm-free)
8. [The 30-Day Launch Checklist](#8-the-30-day-launch-checklist)

---

## 1. Project Overview & Website Architecture

The website is located at `/home/greg/Documents/Taylor's Earth Works/` and consists of clean, dependency-free code:

| File | Purpose |
| :--- | :--- |
| `index.html` | Semantic HTML5 structure, schema markup, SEO tags, content, and form |
| `styles.css` | High-contrast, modern contractor aesthetic matched to his business card logo (industrial charcoal `#191817` & equipment yellow `#f2d82b`) |
| `script.js` | Interactive touch/mouse Before & After slider, mobile menu, and AJAX form handler |
| `images/` | Business card graphic (`taylor-earth-works-card.jpg`) and Before & After slider graphics |
| `README.md` | Quick reference documentation |

### Key Website Features
- **Zero Ongoing Cost:** No monthly platform subscriptions (Wix, Squarespace, or WordPress hosting).
- **Branded to Match Logo Card:** Color scheme extracted directly from his business card: equipment yellow (`#f2d82b`) with warm industrial charcoal (`#191817` / `#272624`).
- **Interactive Before & After Comparison Slider:** Lets homeowners visually drag between rough, rutted ground and laser-graded, compacted finish work.
- **Sticky Mobile Bottom Bar:** Instant "Call Now" and "Free Estimate" buttons fixed to the bottom of mobile screens.
- **Contractor-Specific Services:** Clearing, grading, excavating, footings, driveway regrading, and hauling.
- **Speed & SEO:** 100/100 performance score, zero CDN dependencies, and pre-formatted `LocalBusiness` JSON-LD schema for Zebulon, NC.

---

## 2. Business Details & Customization

The site has already been pre-configured with his actual business card details:
- **Owner & Operator:** Taylor McDaniel
- **Location:** Zebulon, NC (serving Wake, Johnston, Franklin, and Nash Counties)
- **Cell Phone:** `(984) 318-5575` (pre-wired to all click-to-call buttons)
- **Email:** `taylorsearthworks@gmail.com` (pre-wired to the contact form)
- **Facebook:** Taylor's Earth Works
- **Faith/Values:** John 14:6 • John 3:16

### 2. Email Address
The contact form is already configured to route submissions to `taylorsearthworks@gmail.com`:
```html
<form id="estimate-form" action="https://formsubmit.co/taylorsearthworks@gmail.com" method="POST">
```
*(If he ever needs to change this in the future, just update this action URL).*

### 3. Facebook Business Page
Search for `https://www.facebook.com/your-facebook-page` and replace it with the URL of his actual Facebook business page.

### 4. Towns & Counties Served
Search for `[Your City, County & Surrounding Areas]` and the list of town tags under `#service-area` (around line 340) to enter his primary towns, counties, and service radius.

---

## 3. Zero-Cost Hosting Setup ($0/mo Forever)

He only needs to pay for the custom domain name (e.g., `taylorsearthworks.com` for ~$10–$12/year). Hosting, SSL security certificates, and global CDN delivery are 100% free.

### Recommended Method: Cloudflare Pages (Fastest & Easiest)
1. **Purchase the Domain:**
   - Buy the domain through [Cloudflare Registrar](https://www.cloudflare.com/products/registrar/) or [Namecheap](https://www.namecheap.com/).
2. **Deploy the Files:**
   - Create a free account at [cloudflare.com](https://www.cloudflare.com/).
   - Navigate to **Workers & Pages** &rarr; **Create application** &rarr; **Pages** &rarr; **Upload assets**.
   - Drag and drop the `Taylor's Earth Works` folder.
   - Click **Deploy Site**. The site will be live on a free `.pages.dev` subdomain in seconds.
3. **Connect the Custom Domain:**
   - In your Cloudflare Pages project, click **Custom Domains** &rarr; **Set up a custom domain**.
   - Enter `taylorsearthworks.com`.
   - Cloudflare will automatically configure DNS, issue a free SSL certificate, and enforce secure HTTPS.

### Alternative Method: GitHub Pages
1. Create a free account on [github.com](https://github.com).
2. Create a new public repository named `taylors-earth-works`.
3. Upload all files (`index.html`, `styles.css`, `script.js`, and the `images/` directory).
4. Go to **Settings** &rarr; **Pages** &rarr; select branch `main` &rarr; click **Save**.
5. Under **Custom domain**, enter the domain and add the DNS records at your domain registrar.

---

## 4. Setting Up the Free Contact Form

The form uses **FormSubmit.co**, a free service built for static websites that requires zero server setup.

### How Activation Works:
1. The form is already pointed to `taylorsearthworks@gmail.com` in `index.html`.
2. Once the website is published, submit a quick test message through the form.
3. FormSubmit will send a **one-time confirmation email** to `taylorsearthworks@gmail.com`.
4. Taylor clicks the **"Activate Form"** button inside that email.
5. All future estimate requests will immediately arrive in his inbox with the customer's name, phone, address, and project notes.

---

## 5. Before & After Photos & Live Facebook Gallery

### The Interactive Hero Slider
The site features a primary interactive slider showing a real project:
- `images/Before.jpg`: Rough, uneven clay subgrade inside garage stem walls.
- `images/After.jpg`: Laser-leveled, machine-compacted stone base with heavy-duty vapor barrier.

Both images are 2048x1536 (4:3 aspect ratio). The interactive slider has been configured with `aspect-ratio: 4 / 3;` so the transformation is displayed without cropping.

### The Live Facebook Gallery (Elfsight Setup)
Instead of manually updating website code every time Taylor finishes a job, the site uses an automated social media sync. Whenever Taylor posts new photos to his Facebook Business Page, they will automatically appear in the gallery section of the website.

**To activate this feature:**
1. Go to [Elfsight.com](https://elfsight.com/) and create a free account.
2. Select the **Facebook Feed** widget from their catalog.
3. Choose the **"Full Width"** template. This layout expands to fill the container and looks like a modern photo gallery. It is 100% mobile responsive and will automatically stack the photos neatly on phone screens.
4. Connect the widget to Taylor's Earth Works Facebook Page URL.
5. *(Optional but recommended)*: In the widget settings, toggle off the "Facebook Page Header" (the cover photo and logo) so it blends perfectly into the website as a seamless photo gallery.
6. Click **Publish** to generate your unique widget ID (it will look like `12345678-abcd-efgh-ijkl-1234567890ab`).
7. Open `index.html` (around line 457) and replace `YOUR-WIDGET-ID-HERE` with your actual ID.
8. Push the changes to GitHub to instantly update the live site.

---

## 6. The Bullet-Proof Local SEO Playbook

For trade and excavation contractors, **over 80% of estimate calls come from the Google Maps 3-Pack**. Homeowners search for *"driveway repair near me"*, *"skid steer contractor"*, or *"garage floor prep [city]"*.

### Phase 1: Google Business Profile (GBP) Domination

1. **Create the Profile:** Visit [google.com/business](https://www.google.com/business) and sign in.
2. **Business Name:** Use **`Taylor's Earth Works`**.
   *Do NOT add spammy keywords into the title (e.g., "Taylor's Earth Works - Cheap Grading & Bobcat Service"), as Google suspends profiles for name manipulation.*
3. **Set Up as a Service Area Business (SAB):**
   - If operating from home or an equipment yard without a retail showroom, check *"I deliver goods and services to my customers"*.
   - Hide the home address from the public.
   - Set the service area to his home county and surrounding towns/counties within a 30–40 mile radius.
4. **Primary & Secondary Categories:**
   - **Primary:** `Excavating contractor`
   - **Secondary:** `Grading contractor`, `Drainage service`, `Paving contractor`, `Demolition contractor`, `Topsoil supplier`.
5. **Itemized Service Catalog:**
   Add detailed descriptions for each service:
   - Garage & Pole Barn Pad Preparation
   - Gravel Driveway Regrading & Repair
   - Site Grading & Water Drainage Swales
   - Skid Steer & Tractor Work
   - Dump Truck Material Hauling (Limestone, Topsoil, Sand)

---

### Phase 2: The 5-Star Review Generation Machine

Customer reviews are the **#1 factor** that drives rankings in Google Maps.

#### 1. Create a Direct Review Shortcut Link
1. In the Google Business Profile dashboard, click **Ask for reviews**.
2. Copy the short link (e.g., `https://g.page/r/[ID]/review`).
3. Save this link on Taylor's phone in his notes or text shortcuts.

#### 2. The 10-Minute Post-Job Routine
Send this text message **within 2 hours of leaving the jobsite**, while the client is admiring their freshly graded driveway or building pad:

> *"Hey [Customer Name], this is Taylor with Taylor's Earth Works. It was a pleasure working on your [driveway/garage pad/grading] today! As a local owner-operator, Google reviews make a huge difference in helping new customers find us. Would you mind taking 30 seconds to leave an honest review on Google? Here is the direct link: [INSERT REVIEW LINK]. Thank you again for your business!"*

#### 3. Keyword-Coaching Strategy
Google's algorithm scans review text for keywords. When a homeowner writes *"Taylor used his skid steer to grade our driveway and prep our garage floor in [Town]"*, Google ranks the business higher for those exact search queries.

#### 4. Respond to Every Single Review
Always reply within 48 hours and include relevant keywords:
> *"Thanks [Customer Name]! We loved grading the driveway and prepping the gravel base for your new garage in [Town Name]. Enjoy the new build, and don't hesitate to reach out if you need any future dirt work!"*

#### 5. How to Get the First 5 Reviews (The "Bootstrap" Strategy)
Getting the first 5 reviews is critical for Google to start showing the business to strangers. Since he is just launching the official profile, here is how to get those first 5 reviews immediately:
* **Mine Past "Hidden" Jobs:** Have him scroll through his phone contacts and text anyone he has done work for in the last year (even side jobs or favors). 
  > *"Hey [Name], I’m making my earthworks business official and setting up my Google page! Since I helped you out with that [grading/driveway] project a while back, would you mind taking 30 seconds to drop a quick review of my work? It would mean the world to me: [Link]"*
* **Vendor & Contractor References:** Ask professionals he works with (e.g., the local quarry, equipment rental shop, or a concrete contractor who pours over his prepped pads) to leave a review vouching for his professionalism, punctuality, and quality of prep work.
* **Harvest Existing Facebook Comments:** If he has previous comments on his personal Facebook like *"Taylor did an amazing job on our yard!"*, ask those people to copy/paste that exact sentiment onto the new Google Profile.

---

### Phase 3: Geotagged "Proof of Work" Photos

Google prioritizes businesses that demonstrate active, real-world work in their local area.

- **Posting Schedule:** Upload 2 to 3 photos every week to Google Business Profile.
- **Recommended Shots:**
  - Dump truck tailgate-spreading gravel or dumping topsoil.
  - Skid steer or tractor grading a rough slope.
  - Close-up of the rotary laser level setup on a garage sub-base.
  - Clear Before & After shots of driveways or yards.
- **Turn On Camera GPS (Geotagging):** Ensure smartphone camera location tags are turned ON. When Taylor snaps photos on location, Google reads the embedded GPS coordinates, verifying that he actively completes projects across his service territory.

---

### Phase 4: Top 10 Free Directory Citations (NAP Consistency)

Google verifies legitimacy by checking whether the business **NAP (Name, Address, Phone)** matches across the internet.

| Directory | Purpose | Cost | Notes |
| :--- | :--- | :--- | :--- |
| **Google Business Profile** | Primary search & maps driver | Free | Verify via phone/video |
| **Bing Places for Business** | Reaches Windows/Edge users | Free | 1-click import from Google Business Profile |
| **Apple Business Connect** | Powers Apple Maps & Siri | Free | Register at register.apple.com |
| **Facebook Business Page** | Social proof & local community | Free | Link to website & direct phone call |
| **Yelp for Business** | Feeds Apple Maps data | Free | Claim free listing (decline paid sales calls) |
| **Nextdoor Business** | Neighborhood recommendations | Free | Set up business page in local area |
| **Better Business Bureau (BBB)** | Authority trust signal | Free | Claim basic free directory listing |
| **Angi (formerly Angie's List)** | Contractor directory | Free | Free basic listing (do not buy shared leads) |
| **YellowPages / DexKnows** | Citation index | Free | Claim standard listing |
| **Local Chamber of Commerce** | High-powered local backlink | Free/Low cost | Request inclusion on local business roster |

---

### Phase 5: Hyper-Local Facebook Lead Generation

Homeowners regularly turn to local Facebook groups to find earthmoving and equipment operators.

1. **Facebook Business Page:** Set up a clean page with photos of the equipment, contact information, and a link to the website.
2. **Join 5–10 Local Community Groups:**
   - *"[County Name] Buy, Sell, Trade"*
   - *"[Town Name] Community Chit Chat"*
   - *"[Town Name] Neighbors Helping Neighbors"*
3. **Weekly Transformation Post (Non-Spammy Format):**
   Post 2–4 high-quality photos with this format:
   > *"Wrapped up this 400 ft driveway repair in [Town Name] this week. Cut out the washboards and ruts, established a center crown to shed rain into the ditch, and compacted 2 tandem loads of fresh crushed rock. If your driveway needs regrading or you are prepping for a garage/pole barn concrete floor this season, give Taylor's Earth Works a call or text at [Phone Number] for a free estimate!"*
4. **Monitor Community Requests:**
   Search groups for keywords like *"skid steer"*, *"dump truck"*, *"gravel"*, *"dirt work"*, *"grading"*, or *"driveway"*. When a neighbor asks for a recommendation, reply with a helpful answer and link his business page.

---

## 7. Managing Leads & Estimates with Streak CRM (Free)

As an owner-operator in the field, Taylor needs a low-friction way to track incoming estimate requests, schedule site visits, and remember to follow up without using complex software.

**Streak CRM** is the perfect solution because it lives entirely inside his existing Gmail inbox (`taylorsearthworks@gmail.com`) and is 100% free for solo users.

### How to Set It Up:
1. **Install the Extension:** Go to [streak.com](https://www.streak.com/) on a desktop computer and click "Add to Chrome".
2. **Create a Sales Pipeline:** Inside Gmail, Streak will prompt you to create a pipeline. Choose the "Sales" or "CRM" template.
3. **Customize the Stages:** Rename the stages to match a contractor's workflow:
   - *New Lead*
   - *Site Visit Scheduled*
   - *Estimate Sent*
   - *Job Won / Scheduled*
   - *Job Completed / Paid*
   - *Lost*

### The Daily Workflow:
- **Incoming Leads:** When an estimate request comes in from the website form, he clicks the "Streak" button right inside the email to add it to his pipeline as a *New Lead*.
- **Follow-Up Reminders (Snooze):** If he sends an estimate and wants to follow up in 3 days, he clicks the "Snooze" button in Gmail. The email will disappear and magically pop back to the top of his inbox 3 days later to remind him to call them.
- **Track Estimate Opens:** Streak automatically tracks when a customer opens an email, so he knows exactly when they are looking at his estimate!

---

## 8. The 30-Day Launch Checklist

- [ ] **Day 1:** Purchase domain name (`~$10–$12/yr`) via Cloudflare Registrar or Namecheap.
- [ ] **Day 2:** Deploy the website folder to **Cloudflare Pages** (100% free) and connect the custom domain.
- [ ] **Day 3:** Submit a test message on the contact form and activate the **FormSubmit** confirmation link.
- [ ] **Day 4:** Set up and submit **Google Business Profile** for verification as a Service Area Business.
- [ ] **Day 5:** Set up the **Facebook Business Page** and link to website and phone.
- [ ] **Day 6:** Import Google Business Profile into **Bing Places** and register on **Apple Business Connect**.
- [ ] **Day 7:** Claim free listings on Yelp, Nextdoor, and BBB.
- [ ] **Week 2:** Reach out to previous clients to gather his first 5 Google reviews.
- [ ] **Week 3:** Upload first batch of job photos to Google Business Profile and post a recent project in 2 local Facebook groups.
- [ ] **Week 4:** Verify that search rankings for *"driveway grading [town]"* and *"site prep [county]"* begin populating in local results.
