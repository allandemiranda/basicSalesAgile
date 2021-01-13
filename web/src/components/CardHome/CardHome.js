import React from 'react';
import clsx from 'clsx';
import PropTypes from 'prop-types';
import { makeStyles } from '@material-ui/styles';
import { Card, Typography, Avatar } from '@material-ui/core';

const useStyles = makeStyles(theme => ({
  root: {
    padding: theme.spacing(3),
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'space-between'
  },
  details: {
    display: 'flex',
    alignItems: 'center',
    flexWrap: 'wrap'
  },
  label: {
    marginLeft: theme.spacing(1)
  },
  avatar: {
    height: 48,
    width: 48
  }
}));

const CardHome = props => {
  const { className, value, symbol, icon, backgroundImage, title, ...rest } = props;

  const classes = useStyles();

  return (
    <Card
      {...rest}
      className={clsx(classes.root, className)}
    >
      <div>
        <Typography
          component="h3"
          gutterBottom
          variant="overline"
        >
          {title}
        </Typography>
        <div className={classes.details}>
          <Typography variant="h3">
            {symbol}
            {' '}
            {value}
          </Typography>
        </div>
      </div>
      <Avatar
        className={classes.avatar}
        style={{backgroundImage}}
      >
        {icon}
      </Avatar>
    </Card>
  );
};

CardHome.propTypes = {
  backgroundImage: PropTypes.string,
  className: PropTypes.string,
  icon: PropTypes.node,
  symbol: PropTypes.string,
  title: PropTypes.string,
  value: PropTypes.number,  
};

export default CardHome;
