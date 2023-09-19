const Navbar = () => {
    return (
        <nav className="navbar">
            <a href="/" className="site-title">Site Name</a>
            <ul className="">
                <li>
                    <a href="/pricing">Pricing</a>
                </li>
                <li>
                    <a href="/about">About</a>
                </li>
            </ul>
        </nav>
    )
}

export default Navbar;