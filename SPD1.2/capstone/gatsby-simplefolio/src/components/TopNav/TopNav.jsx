import React from 'react';
import Nav from 'react-bootstrap/Nav';
import { Link } from 'react-scroll';

const TopNav = () => {
  return (
    <>
      <Nav className="justify-content-center" activeKey="/home">
        <Link to="about" smooth duration={1000}>
          <Nav.Item>
            <Nav.Link
              eventKey="link-1"
              style={{ color: '#02aab0', fontWeight: 600, margin: '20px 20px 0px 20px' }}
            >
              About
            </Nav.Link>
          </Nav.Item>
        </Link>
        <Link to="projects" smooth duration={1000}>
          <Nav.Item>
            <Nav.Link
              eventKey="link-1"
              style={{ color: '#02aab0', fontWeight: 600, margin: '20px 20px 0px 20px' }}
            >
              Projects
            </Nav.Link>
          </Nav.Item>
        </Link>
        <Link to="contact" smooth duration={1000}>
          <Nav.Item>
            <Nav.Link
              eventKey="link-1"
              style={{ color: '#02aab0', fontWeight: 600, margin: '20px 20px 0px 20px' }}
            >
              Contact
            </Nav.Link>
          </Nav.Item>
        </Link>
      </Nav>
    </>
  );
};

export default TopNav;
