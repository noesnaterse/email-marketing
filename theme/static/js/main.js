document.querySelector("#user-menu-button").addEventListener("mouseover", () => {
    document.querySelector("#user-menu").classList.remove("hidden");
    document.querySelector("#user-menu").classList.add("transition");
    document.querySelector("#user-menu").classList.add("ease-out");
    document.querySelector("#user-menu").classList.add("duration-100");
});

document.querySelector("#user-menu").addEventListener("mouseleave", () => {
    document.querySelector("#user-menu").classList.add("hidden");
});
