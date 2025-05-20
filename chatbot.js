document.addEventListener("DOMContentLoaded", () => {
    // Wait until wp.data is ready
    if (typeof wp !== 'undefined' && wp.data && wp.data.select) {
        const user = wp.data.select('core').getCurrentUser();
        console.log("Current user:", user);
    } else {
        console.warn("wp.data is not available");
    }
});
