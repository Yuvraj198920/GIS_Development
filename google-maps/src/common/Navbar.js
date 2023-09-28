import "./navbar.css"
function Navbar() {
    return(
        <nav>
            <div className="logo">
                <i className="fas fa-mountain"></i>
                <h4>Mountains</h4>
            </div>
            <ul className="navlinks">
                <li className="links"><a href="#">Home</a></li>
                <li className="links"><a href="#">About</a></li>
                <li className="links"><a href="#">Services</a></li>
                <li className="links"><a href="#">Contact Us</a></li>
            </ul>
        </nav>
    )
}

export default Navbar;