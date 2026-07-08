import os
from django.core.management.base import BaseCommand
from jobs.models import Profile, skills, Job, ProjectGalleryImage, Experience, Education, Certificate

class Command(BaseCommand):
    help = 'Seeds initial portfolio data personalized for Pravallika Kudirilla'

    def handle(self, *args, **options):
        self.stdout.write("Starting database seeding...")
        
        # 1. Clear existing database
        Profile.objects.all().delete()
        skills.objects.all().delete()
        Job.objects.all().delete()
        ProjectGalleryImage.objects.all().delete()
        Experience.objects.all().delete()
        Education.objects.all().delete()
        Certificate.objects.all().delete()

        self.stdout.write("Existing database records cleared.")

        # 2. Seed Profile (Pravallika Kudirilla)
        profile = Profile.objects.create(
            name="Pravallika Kudirilla",
            email="pravallikakudirilla77@gmail.com",
            location="Hyderabad, India",
            availability="Freelance / Full-time",
            tagline="I design and implement scalable backend engines and full-stack web products. Specializing in Python, Django, containerized deployments, and clean APIs.",
            bio="I am a Backend Developer passionate about building scalable, high-performance web applications using Python, Django, PostgreSQL, Docker, and JavaScript. I enjoy resolving complex engineering problems through clean, robust architecture and modern tools.",
            professions="Full Stack Developer, Python Developer, Django Engineer, Backend Developer",
            github_link="https://github.com/Pravallika-Kudirilla",
            linkedin_link="https://www.linkedin.com/in/pravallika-kudirilla/",
            resume="/static/resume.pdf",
            profile_photo=None # Will fall back to her local profile.png
        )
        self.stdout.write(f"Profile for '{profile.name}' created.")

        # 3. Seed Skills
        skills_data = [
            ("Python", "fa-brands fa-python"),
            ("Flask", "fa-solid fa-flask"),
            ("Django", "fa-solid fa-code"),
            ("JavaScript", "fa-brands fa-js"),
            ("React.js", "fa-brands fa-react"),
            ("HTML5", "fa-brands fa-html5"),
            ("CSS3", "fa-brands fa-css3-alt"),
            ("SQL", "fa-solid fa-database"),
            ("MySQL", "fa-solid fa-database"),
            ("PostgreSQL", "fa-solid fa-database"),
            ("MongoDB", "fa-solid fa-leaf"),
            ("Redis", "fa-solid fa-database"),
            ("SQLite", "fa-solid fa-database"),
            ("Node.js", "fa-brands fa-node-js"),
            ("Docker", "fa-brands fa-docker"),
            ("Git", "fa-brands fa-git-alt"),
            ("GitHub", "fa-brands fa-github"),
            ("REST APIs", "fa-solid fa-plug"),
            ("Postman", "fa-solid fa-paper-plane"),
            ("Cloudinary", "fa-solid fa-cloud"),
            ("Firebase", "fa-solid fa-fire"),
            ("Android Studio", "fa-brands fa-android"),
            ("Figma", "fa-brands fa-figma"),
            ("JSON", "fa-solid fa-code")
        ]
        
        skill_objs = {}
        for name, icon in skills_data:
            skill_objs[name.lower()] = skills.objects.create(skill=name, icon_class=icon)
        self.stdout.write(f"Seeded {len(skills_data)} skills.")

        # 4. Seed Experiences
        exp1 = Experience.objects.create(
            role="Web Development Intern",
            company="INTERNSHALA",
            start_date="Apr 2025",
            end_date="Jun 2025",
            description="A responsive PG accommodation portal featuring user authentication, city-based PG listings, smart filtering, and dynamic content rendering. Developed using HTML, CSS, JavaScript, PHP, and MySQL with a focus on usability across devices."
        )
        exp1.technologies.add(skill_objs["react.js"], skill_objs["sql"])

        exp2 = Experience.objects.create(
            role="Full-Stack Development Intern",
            company="Embrizon Technologies",
            start_date="Sep 2024",
            end_date="Nov 2024",
            description="Designed and developed a responsive e-commerce platform with secure user authentication, product management, and database connectivity. Focused on delivering an intuitive user experience through responsive UI and efficient backend integration."
        )
        exp2.technologies.add(skill_objs["sql"])
        self.stdout.write("Seeded experiences.")

        # 5. Seed Education
        Education.objects.create(
            degree="Bachelor of Technology in Computer Science",
            college="Anil Neerukonda Institute of Technology and Sciences",
            date_range="2024-2027",
            cgpa="8.78"
        )
        Education.objects.create(
            degree="Electronics and Communication Engineering",
            college="Government Polytechnic, Pendurthi",
            date_range="2021-2024",
            cgpa="8.9"
        )
        self.stdout.write("Seeded education history.")

        # 6. Seed Certificates
        certs_data = [
            ("Django Developer", "LinkedIn Learning", "2026", "https://www.linkedin.com/learning/certificates/8ff352ca02f876e5fa949d04aaa9b9fa389437e9336375615c51a79b74aff0bd?trk=share_certificate"),
            ("Associate Software Operator", "Redis", "2026", "https://university.redis.io/certificate/un4fp9to6r5aip"),
            ("API Testing", "LinkedIn Learning", "2026", "https://www.linkedin.com/learning/certificates/a257d1951da86d1d62feef108f1a80ed51c09eeef5492a7505f2aada2fa16f79"),
            ("Docker", "Docker", "2026", "https://www.linkedin.com/learning/certificates/6dbd006a443d77a5e56ffeadd1d9935737f15a590b9e582e8c71d2d9e63bf10b"),
            ("Web Development", "Internshala", "2025", "https://trainings.internshala.com/certificate/view/nsdc/5b9qe7y1b4a/dkp8nfzd73e/"),
            ("Software Engineer Intern Certificate", "HackerRank", "2025", "https://www.hackerrank.com/certificates/238582432955"),
            ("How To CSS", "Codekaro", "2024", "https://codekaro.in/course-certificate/0253eb6ed55f25796")
        ]
        
        for title, org, year, link in certs_data:
            Certificate.objects.create(title=title, organization=org, year=year, verification_link=link)
        self.stdout.write("Seeded certificates.")

        # 7. Seed Jobs (Projects) with Order settings
        job1 = Job.objects.create(
            title="Resufit – AI-Powered Resume Analyzer, Job Fit Analyzer & Resume Builder",
            summary="To develop a secure, full-stack web application that leverages Generative AI and OCR technology to help job seekers build, analyze, and automatically tailor their resumes to match target job descriptions.",
            overview="ResuFit is an AI-powered resume analysis web application that helps job seekers optimize their resumes for Applicant Tracking Systems (ATS). Users can upload their resume and compare it with a job description to receive a detailed compatibility score, identify missing skills, and get personalized recommendations for improvement. Built using Flask, HTML, CSS, JavaScript, and SQLite, the application combines an intuitive user interface with AI-driven analysis to help users create stronger, ATS-friendly resumes.",
            features="AI-Powered Resume Analysis\nATS Compatibility Scoring\nJob Description Matching\nPersonalized Resume Improvement Suggestions\nMissing Skills Identification\nResume File Upload (PDF)\nSecure User Authentication\nGoogle OAuth Login\nResume Analysis History\nResponsive and User-Friendly Interface\nFast AI-Powered Processing\nCross-Device Compatibility",
            challenges="Implementing accurate AI-based resume analysis\nExtracting and processing text from PDF resumes\nComparing resumes with job descriptions effectively\nGenerating meaningful ATS improvement suggestions\nIntegrating Google OAuth for secure authentication\nManaging user sessions and authentication flow\nEnsuring fast response times for AI analysis\nDesigning a responsive and intuitive user interface\nHandling file upload validation and error cases\nMaintaining data security and user privacy",
            github_link="https://github.com/bharathkumarkarri/Resufit",
            live_link="https://resufit-517i.onrender.com/",
            is_featured=True,
            status="Completed",
            published_date="June 2026",
            image="utzmlnrhgcw5npl7my0t",
            order=0
        )
        job1.technologies.add(
            skill_objs["python"], skill_objs["flask"], skill_objs["sqlite"],
            skill_objs["rest apis"], skill_objs["html5"], skill_objs["css3"], skill_objs["javascript"]
        )

        job2 = Job.objects.create(
            title="Personal Portfolio",
            summary="This premium developer portfolio is built using Python and Django 6, styled with beach-themed minimalist Vanilla CSS, integrated with a PostgreSQL database, powered by Cloudinary for asset hosting, and deployed on Render.",
            overview="This premium developer portfolio is built using Python and Django 6, styled with beach-themed minimalist Vanilla CSS, integrated with a PostgreSQL database, powered by Cloudinary for asset hosting, and deployed on Render with Gunicorn and WhiteNoise for production-ready performance.",
            features="Dynamic typing animation\nInteractive mouse tracking glowing spotlight\nMinimalist modern beach design theme\nEditable models via Django Admin\nResponsive design across mobile and desktop\nCustom lightboxes and collapsible lists",
            challenges="Creating smooth interactive mouse spotlight tracking\nEnsuring clean responsive typography transitions\nConfiguring Cloudinary for static and media assets handling",
            github_link="https://github.com/Pravallika-Kudirilla",
            live_link="https://portfolio-nhf3.onrender.com",
            is_featured=True,
            status="Completed",
            published_date="June 2026",
            image="mcvnxll9bsvthwemgzde",
            order=1
        )
        job2.technologies.add(
            skill_objs["python"], skill_objs["html5"], skill_objs["css3"],
            skill_objs["javascript"], skill_objs["django"], skill_objs["postgresql"], skill_objs["cloudinary"]
        )

        job3 = Job.objects.create(
            title="E-commerce Website",
            summary="To design and develop a premium, interactive web experience that elevates brand storytelling, showcases custom craftsmanship, and drives customer engagement through intuitive navigation.",
            overview="To design and develop a premium, interactive web experience that elevates brand storytelling, showcases custom craftsmanship, and drives customer engagement through intuitive navigation and a seamless checkout process.",
            features="Interactive shopping cart\nResponsive layouts for all screen sizes\nSmooth animations and transitions",
            challenges="Managing state transitions for checkout flows\nDesigning fluid minimalist product layouts",
            github_link="https://github.com/Pravallika-Kudirilla",
            live_link="",
            is_featured=False,
            status="Completed",
            published_date="May 2025",
            image="frx7txyls0ls5ljybkor",
            order=2
        )
        job3.technologies.add(
            skill_objs["html5"], skill_objs["css3"], skill_objs["javascript"]
        )
        self.stdout.write("Seeded projects/jobs.")

        # 8. Seed Project Gallery Images for Project 1 (Resufit)
        gallery_images = [
            ("d7gkgelyxyrv2wx9kich", "Home"),
            ("thvbbfozwgj8vllhgzyu", "Dashboard"),
            ("xu3whui0gywf3s8qiqgy", "JobFit Analyzer"),
            ("zd0samuxfldacy18zvhq", "Resume Builder"),
            ("c9lhchooybbgct152pup", "Resume"),
            ("ip5evqoeflvc2cg9ifjm", "Resume Tailoring")
        ]
        for img_id, caption in gallery_images:
            ProjectGalleryImage.objects.create(
                project=job1,
                image=img_id,
                caption=caption
            )
        self.stdout.write("Seeded project gallery images.")
        
        self.stdout.write(self.style.SUCCESS("Database seeding completed successfully!"))
