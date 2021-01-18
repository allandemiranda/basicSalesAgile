import React from 'react';
import {
  AppBar,
  Toolbar,
  Container,
  Typography  
} from '@material-ui/core';

const FooterBar = () => {
  return (
    <AppBar 
      color="primary"
      position="static"
    >
      <Container maxWidth="lg">
        <Toolbar variant="dense">
          <Typography 
            color="inherit"
            variant="body1"
          >
            © 2021 Agile Solutions
          </Typography>
        </Toolbar>
      </Container>
    </AppBar>
  );
};

export default FooterBar;
