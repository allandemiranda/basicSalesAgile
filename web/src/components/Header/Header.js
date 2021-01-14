import React from 'react';
import PropTypes from 'prop-types';
import clsx from 'clsx';
import { makeStyles } from '@material-ui/styles';
import { Typography, Grid } from '@material-ui/core';


const useStyles = makeStyles(theme => ({
  root: {},
  dates: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'flex-end'
  },
  calendarTodayIcon: {
    marginRight: theme.spacing(1)
  }
}));

const Header = props => {
  const { className, titleName, titleSecond, ...rest } = props;

  const classes = useStyles();  

  return (
    <div
      {...rest}
      className={clsx(classes.root, className)}
    >
      <Grid
        container
        justify="space-between"
        spacing={3}
      >
        <Grid
          item
          lg={6}
          xs={12}
        >
          <Typography
            component="h2"
            gutterBottom
            variant="overline"
          >
            {titleSecond}
          </Typography>
          <Typography
            component="h1"
            gutterBottom
            variant="h3"
          >
            {titleName}
          </Typography>
        </Grid>        
      </Grid>
    </div>
  );
};

Header.propTypes = {
  className: PropTypes.string,
  titleName: PropTypes.string,
  titleSecond: PropTypes.string
};

Header.defaultProps = {};

export default Header;
