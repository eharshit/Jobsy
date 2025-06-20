import os

def format_to_markdown(internships, output_path="output/job_dump.md"):
    # Make sure the directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# 🔍 Latest Internship Opportunities via Opdrop\n\n")

        if not internships:
            f.write("No internships found.\n")
            return

        for i, job in enumerate(internships, 1):
            f.write(f"### {i}. [{job['title']}]({job['link']})\n")
            f.write(f"**Company:** {job['company']}\n\n")
            f.write(f"📍 {job['location']} | 💰 {job['stipend']} | ⏳ {job['duration']}\n")
            f.write("---\n\n")
