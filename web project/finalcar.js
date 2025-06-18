<script>
// 1. Auto Year Update in Footer
const yearSpan = document.createElement("span");
yearSpan.textContent = ` ${new Date().getFullYear()} `;
document.querySelector("footer").innerHTML = "&copy;" + yearSpan.textContent + " B M W. All rights reserved." + document.querySelector("footer").innerHTML.split("All rights reserved.")[1];

// 2. Alert When "See More" Links Are Clicked
document.querySelectorAll(".see-more").forEach(btn => {
    btn.addEventListener("click", function () {
        alert("You are about to visit the official BMW website.");
    });
});

// 3. Back-to-Top Button
const topBtn = document.createElement("button");
topBtn.textContent = "↑ Top";
topBtn.style.position = "fixed";
topBtn.style.bottom = "20px";
topBtn.style.right = "20px";
topBtn.style.padding = "10px 15px";
topBtn.style.backgroundColor = "#111";
topBtn.style.color = "#fff";
topBtn.style.border = "none";
topBtn.style.borderRadius = "5px";
topBtn.style.cursor = "pointer";
topBtn.style.display = "none";
topBtn.style.zIndex = "1000";
document.body.appendChild(topBtn);

window.addEventListener("scroll", () => {
    topBtn.style.display = window.scrollY > 300 ? "block" : "none";
});
topBtn.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
});

// 4. Hero Title Animation
const heroTitle = document.querySelector(".hero h2");
let opacity = 0;
heroTitle.style.opacity = opacity;
const fadeIn = setInterval(() => {
    opacity += 0.02;
    heroTitle.style.opacity = opacity;
    if (opacity >= 1) clearInterval(fadeIn);
}, 40);

// 5. Show Current Date in Contact Section
const contactSection = document.querySelector("#contact");
const today = new Date().toLocaleDateString();
const dateP = document.createElement("p");
dateP.textContent = `Today's Date: ${today}`;
dateP.style.fontStyle = "italic";
dateP.style.marginTop = "10px";
contactSection.appendChild(dateP);
</script>
